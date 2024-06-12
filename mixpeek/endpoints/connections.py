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
        
        # mixpeek.connections.data.insert(connection_id="123", payload={"key": "value"})
        def insert(self, connection_id: str, payload: list):
            pass

        # mixpeek.connections.data.delete(connection_id="123", filters={"key": "value"})
        def delete(self, connection_id: str, filters: dict):
            pass

        # mixpeek.connections.data.upsert(connection_id="123", payload={"key": "value"}, filters={"key": "value"})
        def upsert(self, connection_id: str, payload: dict, filters: dict):
            pass
            
        
