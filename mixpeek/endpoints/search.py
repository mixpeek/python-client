import requests
import os
import json

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

    # def upload(self, file_path, filters=None, page=1, page_size=10):
    #     try:
    #         url = f"{self.base_url}search/upload"
            
    #         filename = os.path.basename(file_path)
    #         files = {
    #             'file': (filename, open(file_path, 'rb'), 'application/octet-stream')
    #         }
            
    #         payload = {
    #             'filters': json.dumps(filters or {}),
    #             'page': str(page),
    #             'page_size': str(page_size)
    #         }
            
    #         response = requests.post(url, headers=self.headers, data=payload, files=files)
    #         response.raise_for_status()
    #         return response.json()
    #     except requests.RequestException as e:
    #         return {"error": str(e)}

    def url(self, target_url, filters=None, modality="text", page=1, page_size=10):
        try:
            url = f"{self.base_url}search/url"
            data = {
                "url": target_url,
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