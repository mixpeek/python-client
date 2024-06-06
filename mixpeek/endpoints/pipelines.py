import requests

class Pipelines:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create(self, alias: str, code: str, destination: dict, source: dict):
        url = f"{self.base_url}pipelines/"
        data = {
            "alias": alias,
            "code": code,
            "destination": destination,
            "source": source
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    def invoke(self, pipeline_id: str, payload: dict, options: dict):
        url = f"{self.base_url}pipelines/invoke/{pipeline_id}"
        data = {
            "payload": payload,
            "options": options
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()