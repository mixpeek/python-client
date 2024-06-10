import requests

class Extract:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def extract(self, input: str, input_type: str, modality: str = None):
        url = f"{self.base_url}extract/"
        data = {
            "modality": modality,
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()
