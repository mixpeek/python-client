import requests
from magika import Magika


modality_to_content_types = {
    "text": [
        "application/pdf",
        "text/html",
        "text/html; charset=utf-8",
        "text/csv",
        "text/plain",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-powerpoint",
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "text/plain",
        "text/markdown",
        "application/xml",
    ],
    "image": [
        "image/png",
        "image/jpeg",
        "image/gif",
        "image/bmp",
        "image/tiff",
        "image/webp",
    ],
    "audio": [
        "audio/mpeg",
        "audio/wav",
        "audio/ogg",
        "audio/flac",
        "audio/mp4",
        "audio/aac",
        "audio/mp3",
    ],
    "video": [
        "video/mp4",
        "video/x-msvideo",
        "video/quicktime",
        "video/x-ms-wmv",
        "video/x-flv",
    ],
}



class Tools:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.video = self.Video(self)

    def detect(self, url: str):
        # Fetch the file from the URL
        response = requests.get(url)
        content_type = response.headers.get('Content-Type', '').split(';')[0]  # Get the base MIME type without parameters

        # Determine modality based on MIME type and Magika detection
        for modality, types in modality_to_content_types.items():
            if content_type in types:
                return modality
        return 'unknown'

    class Video:
        def __init__(self, parent):
            self.base_url = parent.base_url
            self.headers = parent.headers

        def process(self, url: str, frame_interval: int, resolution: list, return_base64: bool):
            endpoint = f"{self.base_url}tools/video/process"
            data = {
                "url": url,
                "frame_interval": frame_interval,
                "resolution": resolution,
                "return_base64": return_base64
            }
            response = requests.post(endpoint, json=data, headers=self.headers)
            return response.json()