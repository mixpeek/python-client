import requests

class Collections:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def list_files(self, collection_id, randomize=False, page=1, page_size=10, filters=None, sort_by=None, sort_order="asc"):
        try:
            url = f"{self.base_url}collections/"
            data = {
                "collection_id": collection_id,
                "randomize": randomize,
                "page": page,
                "page_size": page_size,
                "filters": filters,
                "sort_by": sort_by,
                "sort_order": sort_order
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def list_collections(self):
        try:
            url = f"{self.base_url}collections/"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def search_files(self, query, collection_id, page=1, page_size=10, sort_by=None, sort_order="asc"):
        try:
            url = f"{self.base_url}collections/search"
            data = {
                "query": query,
                "collection_id": collection_id,
                "page": page,
                "page_size": page_size,
                "sort_by": sort_by,
                "sort_order": sort_order
            }
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_file_by_id(self, file_id):
        try:
            url = f"{self.base_url}collections/file/{file_id}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_full_file(self, file_id):
        try:
            url = f"{self.base_url}collections/file/{file_id}/full"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def delete_file_by_id(self, file_id):
        try:
            url = f"{self.base_url}collections/file/{file_id}"
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def delete_collection(self, collection_id):
        try:
            url = f"{self.base_url}collections/{collection_id}"
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}