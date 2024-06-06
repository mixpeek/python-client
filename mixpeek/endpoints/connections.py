import requests

class Connections:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers
        self.data = self.Data(self)

    def create(self, alias: str, engine: str, details: dict):
        url = f"{self.base_url}connections/"
        data = {
            "alias": alias,
            "engine": engine,
            "details": details
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

    class Data:
        def __init__(self, parent):
            self.base_url = parent.base_url
            self.headers = parent.headers
        
        def insert(self, connection_id: str, payload: dict):
            pass

        def delete(self, connection_id: str, filters: dict):
            pass
            
        
