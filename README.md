# Mixpeek Python SDK

This SDK provides easy access to the Mixpeek API for Python developers.

## Installation

```bash
pip install mixpeek
```

## Usage

First, import and initialize the Mixpeek client:

```python
from mixpeek import Mixpeek

client = Mixpeek(api_key="your_api_key_here")
```

### Embed

The `embed` module provides methods for embedding various types of data.

#### Video Embedding

```python
response = client.embed.video(model_id="model_id", input="video_data", input_type="base64")
```

- `model_id` (str): The ID of the model to use for embedding.
- `input` (str): The video data or URL.
- `input_type` (str): Either "base64" or "url".

#### Text Embedding

```python
response = client.embed.text(model_id="model_id", input="text_to_embed", input_type="text")
```

- `model_id` (str): The ID of the model to use for embedding.
- `input` (str): The text to embed.
- `input_type` (str): Should be "text".

#### Image Embedding

```python
response = client.embed.image(model_id="model_id", input="image_data", input_type="base64")
```

- `model_id` (str): The ID of the model to use for embedding.
- `input` (str): The image data or URL.
- `input_type` (str): Either "base64" or "url".

#### Audio Embedding

```python
response = client.embed.audio(model_id="model_id", input="audio_data", input_type="base64")
```

- `model_id` (str): The ID of the model to use for embedding.
- `input` (str): The audio data or URL.
- `input_type` (str): Either "base64" or "url".

### Index

The `index` module provides methods for indexing various types of content.

#### Upload File

```python
with open("file.txt", "rb") as file:
    response = client.index.upload(file=file, collection_id="collection_id", metadata={"key": "value"}, settings={"video": {"transcribe": True}})
```

- `file` (file object): The file to upload.
- `collection_id` (str): The ID of the collection to add the file to.
- `metadata` (dict, optional): Additional metadata for the file.
- `settings` (dict, optional): Processing settings for the file.

#### Index URL

```python
response = client.index.url(url="https://example.com", collection_id="collection_id", metadata={"key": "value"}, settings={"image": {"caption_model_id": "model_id"}})
```

- `url` (str): The URL to index.
- `collection_id` (str): The ID of the collection to add the content to.
- `metadata` (dict, optional): Additional metadata for the content.
- `settings` (dict, optional): Processing settings for the content.

#### Index YouTube Video

```python
response = client.index.youtube(youtube_video_id="video_id", collection_id="collection_id", metadata={"key": "value"}, settings={"video": {"transcribe": True}})
```

- `youtube_video_id` (str): The ID of the YouTube video to index.
- `collection_id` (str): The ID of the collection to add the video to.
- `metadata` (dict, optional): Additional metadata for the video.
- `settings` (dict, optional): Processing settings for the video.

#### Search YouTube

```python
response = client.index.youtube_search(query="search query", collection_id="collection_id", max_results=20, metadata={"key": "value"}, shorts_only=False)
```

- `query` (str): The search query for YouTube videos.
- `collection_id` (str): The ID of the collection to add the search results to.
- `max_results` (int, optional): Maximum number of results to return (default: 10, max: 500).
- `metadata` (dict, optional): Additional metadata for the search results.
- `shorts_only` (bool, optional): Whether to search for YouTube Shorts only (default: False).

### Search

The `search` module provides methods for searching indexed content.

#### Text Search

```python
response = client.search.text(input="search query", modality="text", input_type="text", filters={"key": "value"}, group_by_file=True, page=1, page_size=10)
```

- `input` (str): The search query or input data.
- `modality` (str): The modality of the search (e.g., "text", "image", "video", "audio").
- `input_type` (str, optional): The type of input (default: "text").
- `filters` (dict, optional): Additional filters for the search.
- `group_by_file` (bool, optional): Whether to group results by file (default: True).
- `page` (int, optional): The page number for pagination (default: 1).
- `page_size` (int, optional): The number of results per page (default: 10).

#### Upload Search

```python
with open("query_image.jpg", "rb") as file:
    response = client.search.upload(file=file, filters={"key": "value"}, page=1, page_size=10)
```

- `file` (file object): The file to use as a search query.
- `filters` (dict, optional): Additional filters for the search.
- `page` (int, optional): The page number for pagination (default: 1).
- `page_size` (int, optional): The number of results per page (default: 10).

#### URL Search

```python
response = client.search.url(url="https://example.com/image.jpg", input_type="file", filters={"key": "value"}, modality="image", page=1, page_size=10)
```

- `url` (str): The URL of the file to use as a search query.
- `input_type` (str, optional): The type of input (default: "file").
- `filters` (dict, optional): Additional filters for the search.
- `modality` (str, optional): The modality of the search (default: "text").
- `page` (int, optional): The page number for pagination (default: 1).
- `page_size` (int, optional): The number of results per page (default: 10).

### Collections

The `collections` module provides methods for managing collections and files.

#### List Files

```python
response = client.collections.list_files(collection_id="collection_id", randomize=False, page=1, page_size=10, filters={"key": "value"}, sort_by="created_at", sort_order="desc")
```

- `collection_id` (str): The ID of the collection to list files from.
- `randomize` (bool, optional): Whether to randomize the results (default: False).
- `page` (int, optional): The page number for pagination (default: 1).
- `page_size` (int, optional): The number of results per page (default: 10).
- `filters` (dict, optional): Additional filters for the file list.
- `sort_by` (str, optional): The field to sort by.
- `sort_order` (str, optional): The sort order, either "asc" or "desc" (default: "asc").

#### List Collections

```python
response = client.collections.list_collections()
```

#### Search Files

```python
response = client.collections.search_files(query="search query", collection_id="collection_id", page=1, page_size=10, sort_by="relevance", sort_order="desc")
```

- `query` (str): The search query for files within the collection.
- `collection_id` (str): The ID of the collection to search in.
- `page` (int, optional): The page number for pagination (default: 1).
- `page_size` (int, optional): The number of results per page (default: 10).
- `sort_by` (str, optional): The field to sort by.
- `sort_order` (str, optional): The sort order, either "asc" or "desc" (default: "asc").

#### Get File by ID

```python
response = client.collections.get_file_by_id(file_id="file_id")
```

- `file_id` (str): The ID of the file to retrieve.

#### Delete File by ID

```python
response = client.collections.delete_file_by_id(file_id="file_id")
```

- `file_id` (str): The ID of the file to delete.

#### Delete Collection

```python
response = client.collections.delete_collection(collection_id="collection_id")
```

- `collection_id` (str): The ID of the collection to delete.

### Tools

The `tools` module provides utility functions for processing various types of data before embedding or indexing.

#### Video Processing

The `video` tool allows you to process video files or URLs into chunks for easier embedding.

```python
from mixpeek import Mixpeek

mixpeek = Mixpeek('your_api_key_here')

video_url = "https://example.com/video.mp4"

# Process video chunks, this runs locally
processed_chunks = mixpeek.tools.video.process(
    video_source=video_url,
    chunk_interval=1,
    resolution=[720, 1280]
)

# Embed each chunk
results = []
for index, chunk in enumerate(processed_chunks):
    print(f"Processing video chunk: {index}")

    embedding = mixpeek.embed.video(
        model_id="vuse-generic-v1",
        input=chunk['base64_chunk'],
        input_type="base64"
    )['embedding']

    result = {
        "start_time": chunk["start_time"],
        "end_time": chunk["end_time"],
        "embedding": embedding
    }
    results.append(result)
    print(f"  Embedding preview: {embedding[:5] + ['...'] + embedding[-5:]}")
    print("Insert into DB here")

print(f"Processed {len(results)} chunks")
```

Parameters for `mixpeek.tools.video.process`:

- `video_source` (str): URL or file path of the video to process.
- `chunk_interval` (float): Duration of each video chunk in seconds.
- `resolution` (list): Desired resolution of the video chunks as [height, width].

The `process` method returns a list of dictionaries, each containing:

- `start_time` (float): Start time of the chunk in seconds.
- `end_time` (float): End time of the chunk in seconds.
- `base64_chunk` (str): Base64-encoded video chunk.

This tool is particularly useful when you need to embed long videos, as it allows you to process the video in smaller chunks and embed each chunk separately.

### Register

The `register` module provides methods for registering various types of data, such as faces for facial recognition.

#### Face Registration

```python
from mixpeek import Mixpeek

# Initialize the Mixpeek client
mixpeek = Mixpeek(api_key="your_api_key_here")

# Path to the local image file containing faces
face_image_path = "/path/to/your/face_image.jpg"

# Start the face registration task
task = mixpeek.register.faces(
    file_path=face_image_path,
    collection_id="face-recognition-collection",
    metadata={"name": "John Doe", "age": 30},
    settings={"detection_threshold": 0.8}
)

# Define a callback function (optional)
def on_task_update(status):
    print(f"Current task status: {status}")

# Wait for the task to complete
status = task.wait_for_done(
    sleep_interval=1,
    callback=on_task_update
)

print(f"Face registration completed with status: {status}")

# If you want to do something with the final result
if status.get("status") == "DONE":
    result = status.get("result")
    print("Face registration result:", result)
else:
    print("Face registration failed or was interrupted")
```

Parameters for `mixpeek.register.faces`:

- `file_path` (str): Path to the local image file containing faces to register.
- `collection_id` (str): The ID of the collection to add the registered faces to.
- `metadata` (dict, optional): Additional metadata for the registered faces.
- `settings` (dict, optional): Processing settings for face registration.

The `faces` method returns a `Task` object that allows you to monitor the progress of the face registration process.

## Response Format

All methods return a JSON response. In case of an error, the response will contain an "error" key with a description of the error.

## Error Handling

The SDK handles HTTP errors and returns them in the response. You should always check for the presence of an "error" key in the response before processing the results.

```python
response = client.embed.text(model_id="model_id", input="text_to_embed", input_type="text")
if "error" in response:
    print(f"An error occurred: {response['error']}")
else:
    # Process the successful response
    print(response)
```

## Rate Limiting

The Mixpeek API may have rate limits. If you encounter rate limiting errors, you should implement appropriate backoff and retry logic in your application.

## Support

For any issues or questions, please contact Mixpeek support or refer to the official API documentation.

```

```
