import requests

from .endpoints.embed import Embed
from .endpoints.collections import Collections
from .endpoints.index import Index
from .endpoints.search import Search
from .endpoints.tools import Tools
from .endpoints.register import Register


class Mixpeek:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.mixpeek.com/"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        # these are remote
        self.embed = Embed(self.base_url, self.headers)
        self.collections = Collections(self.base_url, self.headers)
        self.index = Index(self.base_url, self.headers)
        self.search = Search(self.base_url, self.headers)
        self.register = Register(self.base_url, self.headers)

        # tools is all local
        self.tools = Tools()