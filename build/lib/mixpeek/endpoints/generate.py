import requests
from pydantic import BaseModel

class Generate:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def generate(self, response_format: BaseModel, context: str):
        url = f"{self.base_url}generate/text"
        data = {
            "response_format": response_format.model_json_schema(),
            "context": context
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

