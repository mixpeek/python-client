import requests


class Tools:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.video = self.Video(self)

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