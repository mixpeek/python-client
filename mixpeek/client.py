import requests

from .endpoints.extract import Extract
from .endpoints.embed import Embed
from .endpoints.generate import Generate
from .endpoints.connections import Connections
from .endpoints.tools import Tools
from .endpoints.pipelines import Pipelines


class Mixpeek:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://localhost:8000/"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.extract = Extract(self.base_url, self.headers)
        self.embed = Embed(self.base_url, self.headers)
        self.generate = Generate(self.base_url, self.headers)
        self.connections = Connections(self.base_url, self.headers)
        self.tools = Tools(self.base_url, self.headers)
        self.pipelines = Pipelines(self.base_url, self.headers)
