from .parse.client import ParseClient, \
  AsyncParseClient


class MixpeekParseClient(ParseClient): 

    def text(self, image_filepath: str) -> None:
        pass


class AsyncMixpeekParseClient(AsyncParseClient):

    def text(self, image_filepath: str) -> None:
        pass
