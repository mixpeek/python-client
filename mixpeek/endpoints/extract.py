import requests

class Extract:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def automatic(self, input: str, input_type: str):
        url = f"{self.base_url}extract/"
        data = {
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    def video(self, input: str, input_type: str):
        url = f"{self.base_url}extract/"
        data = {
            "modality": "video",
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()
    
    def audio(self, input: str, input_type: str):
        url = f"{self.base_url}extract/"
        data = {
            "modality": "audio",
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    def image(self, input: str, input_type: str):
        url = f"{self.base_url}extract/"
        data = {
            "modality": "image",
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    def text(self, input: str, input_type: str):
        url = f"{self.base_url}extract/"
        data = {
            "modality": "text",
            "input": input,
            "input_type": input_type
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()