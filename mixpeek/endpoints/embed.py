import requests

class Embed:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def video(self, model_id: str, input: str, input_type: str):
        try:
            url = f"{self.base_url}embed/"
            data = {
                "modality": "video",
                "model_id": model_id,
                "input": input,
                "input_type": input_type
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def text(self, model_id: str, input: str, input_type: str):
        try:
            url = f"{self.base_url}embed/"
            data = {
                "modality": "text",
                "model_id": model_id,
                "input": input,
                "input_type": input_type
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def image(self, model_id: str, input: str, input_type: str):
        try:
            url = f"{self.base_url}embed/"
            data = {
                "modality": "image",
                "model_id": model_id,
                "input": input,
                "input_type": input_type
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def audio(self, model_id: str, input: str, input_type: str):
        try:
            url = f"{self.base_url}embed/"
            data = {
                "modality": "audio",
                "model_id": model_id,
                "input": input,
                "input_type": input_type
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}