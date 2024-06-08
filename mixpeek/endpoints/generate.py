import requests
from pydantic import BaseModel

class Generate:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def text(self, model_id: str, response_format: BaseModel, context: str):
        url = f"{self.base_url}generate/text"
        data = {
            "model_id": model_id,
            "response_format": response_format.schema_json(),  # Ensure correct method to get JSON schema
            "context": context
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()