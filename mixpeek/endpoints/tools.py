import subprocess
import tempfile
import os
import base64
from urllib.parse import urlparse
from urllib.request import urlretrieve
from tqdm import tqdm
from PIL import Image
import io

class Tools:
    def __init__(self):
        self.video = self.Video(self)
        self.image = self.Image(self)

    class Image:
        def __init__(self, parent):
            pass

        def process(self, image_source: str):
            # Download image if it's a URL
            if urlparse(image_source).scheme in ('http', 'https'):
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    urlretrieve(image_source, temp_file.name)
                    image_source = temp_file.name

            # Open and process the image
            with Image.open(image_source) as img:
                # Convert image to RGB mode if it's not already
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                # Convert image to base64
                buffered = io.BytesIO()
                img.save(buffered, format="JPEG")
                base64_string = base64.b64encode(buffered.getvalue()).decode('utf-8')

            # Remove temporary file if it was created
            if urlparse(image_source).scheme in ('http', 'https'):
                os.unlink(image_source)

            return base64_string

    class Video:
        def __init__(self, parent):
            pass

        def process(self, video_source: str, chunk_interval: float, resolution: list):
            chunker = VideoChunker(video_source, chunk_interval, resolution)
            
            for chunk in chunker:
                data = {
                    "base64_chunk": chunk["base64"],
                    "start_time": chunk["start_time"],
                    "end_time": chunk["end_time"]
                }
                yield data


class VideoChunker:
    def __init__(self, video_source, chunk_interval, target_resolution):
        self.video_source = video_source
        self.chunk_interval = chunk_interval
        self.target_resolution = f"{target_resolution[0]}x{target_resolution[1]}"
        self.temp_dir = tempfile.mkdtemp()
        self.total_duration = None
        self.current_time = 0

    def __del__(self):
        self.cleanup()

    def cleanup(self):
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

    def __iter__(self):
        return self

    def __next__(self):
        if self.total_duration is None:
            self._initialize_video()

        chunk = self._process_chunk()
        if chunk is None:
            raise StopIteration
        return chunk

    def _initialize_video(self):
        if urlparse(self.video_source).scheme in ('http', 'https'):
            print("Downloading video...")
            temp_file = os.path.join(self.temp_dir, 'temp_video')
            urlretrieve(self.video_source, temp_file)
            self.video_source = temp_file

        # Get video duration
        result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', self.video_source], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.total_duration = float(result.stdout)
        
        print(f"Total video duration: {self.total_duration:.2f} seconds")
        self.progress_bar = tqdm(total=100, desc="Processing video", unit="%")

    def _process_chunk(self):
        if self.current_time >= self.total_duration:
            return None

        start_time = self.current_time
        end_time = min(start_time + self.chunk_interval, self.total_duration)

        # Generate chunk using FFmpeg
        temp_output = os.path.join(self.temp_dir, f"chunk_{self.current_time}.mp4")
        subprocess.run([
            'ffmpeg', '-y', '-i', self.video_source,
            '-ss', str(start_time), '-to', str(end_time),
            '-vf', f'scale={self.target_resolution}',
            '-c:v', 'libx264', '-preset', 'ultrafast',
            temp_output
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Convert to base64
        with open(temp_output, 'rb') as f:
            base64_string = base64.b64encode(f.read()).decode('utf-8')

        # Remove temporary file
        os.remove(temp_output)

        # Update progress
        progress = (end_time / self.total_duration) * 100
        self.progress_bar.n = int(progress)
        self.progress_bar.refresh()

        self.current_time = end_time

        return {
            "base64": base64_string,
            "start_time": start_time,
            "end_time": end_time
        }