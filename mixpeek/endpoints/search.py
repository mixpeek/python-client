import requests
import os
import json

class Search:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def text(self, query, model_id=None, filters=None, page=1, page_size=10):
        try:
            url = f"{self.base_url}search/text"
            data = {
                "query": query,
                "model_id": model_id,
                "filters": filters or {},
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

    def url(self, target_url, model_id=None, filters=None, page=1, page_size=10):
        try:
            url = f"{self.base_url}search/url"
            data = {
                "url": target_url,
                "model_id": model_id,
                "filters": filters or {},
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