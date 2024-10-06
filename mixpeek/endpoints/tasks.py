import requests
import time

class Task:
    def __init__(self, base_url, headers, task_id):
        self.base_url = base_url
        self.headers = headers
        self.task_id = task_id

    def get_task_status(self, task_id):
        try:
            endpoint = f"{self.base_url}tasks/{task_id}"
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def wait_for_done(self, sleep_interval=2, callback=None):
        while True:
            status = self.get_task_status(self.task_id)
            if callback:
                callback(status)
            if status.get("status") == "DONE":
                return status
            time.sleep(sleep_interval)
