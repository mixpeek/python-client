
import typing
import httpx

from mixpeek.base_client import BaseMixpeek


class Mixpeek(BaseMixpeek): 

    def index(self, image_filepath: str) -> None:
        pass


class AsyncMixpeek(BaseMixpeek):

    def index(self, image_filepath: str) -> None:
        pass