import requests

class Embed:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def video(self, model: str, input: str, input_type: str):
        url = f"{self.base_url}embed/"
        data = {
            "modality": "video",
            "model": model,
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    def text(self, model: str, input: str, input_type: str):
        url = f"{self.base_url}embed/"
        data = {
            "modality": "text",
            "model": model,
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    def image(self, model: str, input: str, input_type: str):
        url = f"{self.base_url}embed/"
        data = {
            "modality": "image",
            "model": model,
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    def audio(self, model: str, input: str, input_type: str):
        url = f"{self.base_url}embed/"
        data = {
            "modality": "audio",
            "model": model,
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()