import requests

class Pipelines:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    # mixpeek.pipelines.enable
    def enable(self, pipeline_id: str, enable: bool):
        url = f"{self.base_url}pipelines/{pipeline_id}/enable"
        data = {
            "enable": enable
        }
        response = requests.patch(url, json=data, headers=self.headers)
        return response.json()

    # mixpeek.pipelines.create
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

    # mixpeek.pipelines.invoke
    def invoke(self, pipeline_id: str, payload: dict, options: dict):
        url = f"{self.base_url}pipelines/invoke/{pipeline_id}"
        data = {
            "payload": payload,
            "options": options
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()