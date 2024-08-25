import requests

class Search:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def text(self, input, modality, input_type="text", filters=None, group_by_file=True, page=1, page_size=10):
        try:
            url = f"{self.base_url}search/text"
            data = {
                "input": input,
                "modality": modality,
                "input_type": input_type,
                "filters": filters or {},
                "group_by_file": group_by_file,
                "pagination": {
                    "page": page,
                    "page_size": page_size
                }
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def upload(self, file, filters=None, page=1, page_size=10):
        try:
            url = f"{self.base_url}search/upload"
            files = {"file": file}
            data = {
                "filters": filters or "{}",
                "page": page,
                "page_size": page_size
            }
            response = requests.post(url, files=files, data=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def url(self, url, input_type="file", filters=None, modality="text", page=1, page_size=10):
        try:
            url = f"{self.base_url}search/url"
            data = {
                "url": url,
                "input_type": input_type,
                "filters": filters or {},
                "modality": modality,
                "pagination": {
                    "page": page,
                    "page_size": page_size
                }
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}