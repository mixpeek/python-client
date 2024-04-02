import pytest
import mixpeek
import typing
import httpx

from mixpeek.client import Mixpeek
from pydantic import BaseModel


class Company(BaseModel):
    name: str


class Companies(BaseModel):
    company_details: typing.List[Company]

# esteininger
# Get started with writing tests with pytest at https://docs.pytest.org
@pytest.mark.skip(reason="This is an example test")
def test_client() -> None:
    client = Mixpeek(base_url="https://api.mixpeek.com", 
                     api_key="<<YOUR_API_KEY>>",
                     httpx_client=httpx.Client(follow_redirects=True))
    response = client.generate(
        model=mixpeek.Model(provider="GPT", model="gpt-3.5-turbo"),
        response_format=Companies,
        context="Please tell me the weather and make sure to respond in the provided JSON schema",
        messages=[],
        settings=mixpeek.Settings()
    )
    print(response)
