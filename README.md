# Mixpeek Python SDK

The Mixpeek Python SDK provides an interface for developers to work with multimodal data, enabling extraction, generation, and embedding of data from various sources, including text, images, video, and audio. This document will guide you through the setup and basic usage of the SDK to get you started with integrating Mixpeek capabilities into your applications.

## Resources

- **Python SDK**: [GitHub Repository](https://github.com/mixpeek/mixpeek-python)
- **API Documentation**: [Mixpeek Docs](https://docs.mixpeek.com/)
- **Support**: [Contact Mixpeek](https://mixpeek.com/contact)
- **Community**: [Join the Community](https://mixpeek.com/community)

## Installation

To get started with the Mixpeek Python SDK, you need to install the package using pip:

```bash
pip install pydantic mixpeek
```

## Getting Started

Before you can use the SDK, you'll need to sign up for Mixpeek and obtain your API key. Once you have your key, you can initialize the client as shown below.

```python
from mixpeek.client import Mixpeek

mixpeek = Mixpeek(api_key="your_api_key_here")
```

### Extract Text from a URL

You can extract text from a file located at a URL using the `extract` method. This is useful for processing documents and obtaining their text content for further analysis or processing.

```python
file_output = mixpeek.extract(
    file_url="https://example.com/path/to/your/document.pdf"
).output

print(file_output)
```

### Handling Large Documents

For large documents, you might prefer to avoid chunking to send the entire corpus into a language model for processing.

```python
full_file_output = mixpeek.extract(
    file_url="https://example.com/path/to/your/large/document.pdf",
    should_chunk=False
).output

print(full_file_output)
```

### Extract Text from a String

Besides files, you can also directly extract text from strings.

```python
str_output = mixpeek.extract(
    contents="Hello world"
).output

print(str_output)
```

### Generate Structured Output

The SDK allows you to generate structured output based on a model. This example shows how to define a model and request a structured response.

```python
from pydantic import BaseModel

class Authors(BaseModel):
    author_email: str

class PaperDetails(BaseModel):
    paper_title: str
    author: Authors

corpus = "Your document text here"

response = mixpeek.generate(
    model={"provider": "GPT", "model": "gpt-3.5-turbo"},
    response_format=PaperDetails,
    context=f"Format this document and adhere to the provided JSON format: {corpus}",
).response

print(response)
```

### Create an Embedding

You can also create embeddings for text, which is useful for similarity comparisons, clustering, and more.

```python
embedding = mixpeek.embed(input="hello world").embedding

print(embedding[:10])  # Print the first 10 elements of the embedding
```
