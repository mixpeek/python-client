import requests
from .tasks import Task

class Register:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def _prepare_data(self, base_data, metadata=None, settings=None):
        if metadata is not None:
            base_data["metadata"] = metadata
        if settings is not None:
            base_data["settings"] = settings
        return base_data

    def faces(self, file_path, collection_id, metadata=None, settings=None):
        try:
            endpoint = f"{self.base_url}register/faces"
            data = self._prepare_data({"collection_id": collection_id}, metadata, settings)
            
            with open(file_path, 'rb') as file:
                files = [('file', (file.name, file, 'application/octet-stream'))]
                response = requests.post(endpoint, headers=self.headers, data=data, files=files)
            
            response.raise_for_status()
            task_id = response.json().get("task_id")
            if task_id:
                return Task(self.base_url, self.headers, task_id)
            else:
                return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
        except IOError as e:
            return {"error": f"File error: {str(e)}"}