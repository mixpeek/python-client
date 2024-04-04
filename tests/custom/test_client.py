import pytest
import mixpeek
from mixpeek.client import Mixpeek
from pydantic import BaseModel
import json

class Authors(BaseModel):
    author_email: str

class PaperDetails(BaseModel):
    paper_title: str
    author: Authors


# esteininger
# Get started with writing tests with pytest at https://docs.pytest.org
@pytest.mark.skip(reason="This is an example test")
def test_client() -> None:
    client = Mixpeek(base_url="https://api.mixpeek.com", 
                     api_key="<<YOUR_API_KEY>>")

    file_output = client.extract(
        file_url="https://mixpeek-public-demo.s3.us-east-2.amazonaws.com/parse/copy-protected.pdf"
    )

    # file_output.output is of type Any, so you have to be careful how you manage it
    corpus = json.dumps(file_output.output)

    str_output = client.extract(
        contents="Hello world"
    )

    print(str_output)

    response = client.generate(
        model={"provider": "GPT", "model": "gpt-3.5-turbo"},
        response_format=PaperDetails,
        context=f"format this document and make sure to respond and adhere to the provided JSON format: {corpus}",
        messages=[],
        settings={"temperature": 0.5},
    )

    print(response)

    embedding = client.embed(input="hello world")
    print(embedding)
