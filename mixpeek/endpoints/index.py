import requests

class Index:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def upload(self, file, collection_id, metadata=None, settings=None):
        try:
            url = f"{self.base_url}index/upload"
            files = {"file": file}
            data = {
                "collection_id": collection_id,
                "metadata": metadata,
                "settings": settings
            }
            response = requests.post(url, files=files, data=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def url(self, url, collection_id, metadata=None, settings=None):
        try:
            url = f"{self.base_url}index/url"
            data = {
                "url": url,
                "collection_id": collection_id,
                "metadata": metadata,
                "settings": settings
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def youtube(self, youtube_video_id, collection_id, metadata=None, settings=None):
        try:
            url = f"{self.base_url}index/youtube"
            data = {
                "youtube_video_id": youtube_video_id,
                "collection_id": collection_id,
                "metadata": metadata,
                "settings": settings
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}