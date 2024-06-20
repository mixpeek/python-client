import requests
import os

class Connections:
    def __init__(self, base_url, headers, api_key):
        self.base_url = base_url
        self.headers = headers
        self.api_key = api_key
        self.data = self.Data(self)
        self.storage = self.Storage(self)

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

        
    class Storage:
        def __init__(self, parent):
            self.base_url = parent.base_url
            self.headers = parent.headers
            self.api_key = parent.api_key

        def upload(self, connection_id: str, file_path: str, prefix: str = None):
            url = f"{self.base_url}connections/storage?connection_id={connection_id}"
            if prefix:
                url += f"&prefix={prefix}"

            files=[
                ('file',(os.path.basename(file_path),open(file_path,'rb'),'application/octet-stream'))
            ]
            headers = {
                'Authorization': f'Bearer {self.api_key}'
            }

            response = requests.request("POST", url, headers=headers, files=files)

            return response.json()


        # mixpeek.connections.storage.delete(connection_id="123", file_name="example.txt")
        def delete(self, connection_id: str, file_name: str):
            url = f"{self.base_url}storage/{connection_id}/delete/{file_name}"
            response = requests.delete(url, headers=self.headers)
            return response.json()


            
        
