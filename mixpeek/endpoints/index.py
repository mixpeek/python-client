import requests

class Index:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def _prepare_data(self, base_data, metadata=None, settings=None):
        if metadata is not None:
            base_data["metadata"] = metadata
        if settings is not None:
            base_data["settings"] = settings
        return base_data

    # def upload(self, file, collection_id, metadata=None, settings=None):
    #     try:
    #         api_url = f"{self.base_url}index/upload"
    #         files = {"file": file}
    #         data = self._prepare_data({"collection_id": collection_id}, metadata, settings)
    #         response = requests.post(api_url, files=files, data=data, headers=self.headers)
    #         response.raise_for_status()
    #         return response.json()
    #     except requests.RequestException as e:
    #         return {"error": str(e)}

    def url(self, target_url, collection_id, metadata=None, settings=None):
        try:
            endpoint = f"{self.base_url}index/url"
            data = self._prepare_data({"url": target_url, "collection_id": collection_id}, metadata, settings)
            response = requests.post(endpoint, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def youtube(self, youtube_video_id, collection_id, metadata=None, settings=None):
        try:
            api_url = f"{self.base_url}index/youtube"
            data = self._prepare_data({"youtube_video_id": youtube_video_id, "collection_id": collection_id}, metadata, settings)
            response = requests.post(api_url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}