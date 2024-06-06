import requests

class Connections:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_connection(self, alias: str, engine: str, details: dict):
        url = f"{self.base_url}connections/"
        data = {
            "alias": alias,
            "engine": engine,
            "details": details
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()
