# Accounts

## Private

Types:

```python
from mixpeek.types.accounts import User
```

Methods:

- <code title="put /accounts/private/">client.accounts.private.<a href="./src/mixpeek/resources/accounts/private.py">update</a>(\*\*<a href="src/mixpeek/types/accounts/private_update_params.py">params</a>) -> <a href="./src/mixpeek/types/accounts/user.py">User</a></code>
- <code title="get /accounts/private/">client.accounts.private.<a href="./src/mixpeek/resources/accounts/private.py">list</a>() -> <a href="./src/mixpeek/types/accounts/user.py">User</a></code>

# Describe

Types:

```python
from mixpeek.types import DescribeUploadResponse, DescribeURLResponse
```

Methods:

- <code title="post /describe/upload">client.describe.<a href="./src/mixpeek/resources/describe.py">upload</a>(\*\*<a href="src/mixpeek/types/describe_upload_params.py">params</a>) -> <a href="./src/mixpeek/types/describe_upload_response.py">object</a></code>
- <code title="post /describe/url">client.describe.<a href="./src/mixpeek/resources/describe.py">url</a>(\*\*<a href="src/mixpeek/types/describe_url_params.py">params</a>) -> <a href="./src/mixpeek/types/describe_url_response.py">object</a></code>

# Embed

Types:

```python
from mixpeek.types import Embeddingresponse
```

Methods:

- <code title="post /embed/">client.embed.<a href="./src/mixpeek/resources/embed.py">create</a>(\*\*<a href="src/mixpeek/types/embed_create_params.py">params</a>) -> <a href="./src/mixpeek/types/embeddingresponse.py">Embeddingresponse</a></code>

# Transcribe

Types:

```python
from mixpeek.types import TranscribeURLResponse
```

Methods:

- <code title="post /transcribe/url">client.transcribe.<a href="./src/mixpeek/resources/transcribe.py">url</a>(\*\*<a href="src/mixpeek/types/transcribe_url_params.py">params</a>) -> <a href="./src/mixpeek/types/transcribe_url_response.py">object</a></code>

# Read

Types:

```python
from mixpeek.types import ReadCreateResponse
```

Methods:

- <code title="post /read/">client.read.<a href="./src/mixpeek/resources/read.py">create</a>() -> <a href="./src/mixpeek/types/read_create_response.py">object</a></code>

# Recognize

Types:

```python
from mixpeek.types import RecognizeCreateResponse
```

Methods:

- <code title="post /recognize/">client.recognize.<a href="./src/mixpeek/resources/recognize.py">create</a>() -> <a href="./src/mixpeek/types/recognize_create_response.py">object</a></code>

# Agent

Types:

```python
from mixpeek.types import Agentresponse
```

Methods:

- <code title="post /agent/">client.agent.<a href="./src/mixpeek/resources/agent/agent.py">create</a>(\*\*<a href="src/mixpeek/types/agent_create_params.py">params</a>) -> <a href="./src/mixpeek/types/agentresponse.py">Agentresponse</a></code>

## Task

Types:

```python
from mixpeek.types.agent import TaskRetrieveResponse
```

Methods:

- <code title="get /agent/{task_id}">client.agent.task.<a href="./src/mixpeek/resources/agent/task.py">retrieve</a>(task_id) -> <a href="./src/mixpeek/types/agent/task_retrieve_response.py">object</a></code>

# Indexes

Types:

```python
from mixpeek.types import IndexFaceResponse, IndexUploadResponse, IndexURLResponse
```

Methods:

- <code title="post /index/face">client.indexes.<a href="./src/mixpeek/resources/indexes.py">face</a>(\*\*<a href="src/mixpeek/types/index_face_params.py">params</a>) -> <a href="./src/mixpeek/types/index_face_response.py">object</a></code>
- <code title="post /index/upload">client.indexes.<a href="./src/mixpeek/resources/indexes.py">upload</a>(\*\*<a href="src/mixpeek/types/index_upload_params.py">params</a>) -> <a href="./src/mixpeek/types/index_upload_response.py">object</a></code>
- <code title="post /index/url">client.indexes.<a href="./src/mixpeek/resources/indexes.py">url</a>(\*\*<a href="src/mixpeek/types/index_url_params.py">params</a>) -> <a href="./src/mixpeek/types/index_url_response.py">object</a></code>

# Search

Types:

```python
from mixpeek.types import SearchTextResponse, SearchUploadResponse, SearchURLResponse
```

Methods:

- <code title="post /search/text">client.search.<a href="./src/mixpeek/resources/search.py">text</a>(\*\*<a href="src/mixpeek/types/search_text_params.py">params</a>) -> <a href="./src/mixpeek/types/search_text_response.py">object</a></code>
- <code title="post /search/upload">client.search.<a href="./src/mixpeek/resources/search.py">upload</a>(\*\*<a href="src/mixpeek/types/search_upload_params.py">params</a>) -> <a href="./src/mixpeek/types/search_upload_response.py">object</a></code>
- <code title="post /search/url">client.search.<a href="./src/mixpeek/resources/search.py">url</a>(\*\*<a href="src/mixpeek/types/search_url_params.py">params</a>) -> <a href="./src/mixpeek/types/search_url_response.py">object</a></code>

# Collections

Types:

```python
from mixpeek.types import CollectionListResponse, CollectionDeleteResponse, CollectionSearchResponse
```

Methods:

- <code title="get /collections/">client.collections.<a href="./src/mixpeek/resources/collections/collections.py">list</a>() -> <a href="./src/mixpeek/types/collection_list_response.py">object</a></code>
- <code title="delete /collections/{collection_id}">client.collections.<a href="./src/mixpeek/resources/collections/collections.py">delete</a>(collection_id) -> <a href="./src/mixpeek/types/collection_delete_response.py">object</a></code>
- <code title="post /collections/search">client.collections.<a href="./src/mixpeek/resources/collections/collections.py">search</a>(\*\*<a href="src/mixpeek/types/collection_search_params.py">params</a>) -> <a href="./src/mixpeek/types/collection_search_response.py">object</a></code>

## Files

Types:

```python
from mixpeek.types.collections import (
    Fileresponse,
    Groupedfiledata,
    FileCreateResponse,
    FileDeleteResponse,
)
```

Methods:

- <code title="post /collections/files">client.collections.files.<a href="./src/mixpeek/resources/collections/files.py">create</a>(\*\*<a href="src/mixpeek/types/collections/file_create_params.py">params</a>) -> <a href="./src/mixpeek/types/collections/file_create_response.py">object</a></code>
- <code title="get /collections/file/{file_id}">client.collections.files.<a href="./src/mixpeek/resources/collections/files.py">retrieve</a>(file_id) -> <a href="./src/mixpeek/types/collections/fileresponse.py">Fileresponse</a></code>
- <code title="put /collections/file/{file_id}">client.collections.files.<a href="./src/mixpeek/resources/collections/files.py">update</a>(file_id, \*\*<a href="src/mixpeek/types/collections/file_update_params.py">params</a>) -> <a href="./src/mixpeek/types/collections/fileresponse.py">Fileresponse</a></code>
- <code title="delete /collections/file/{file_id}">client.collections.files.<a href="./src/mixpeek/resources/collections/files.py">delete</a>(file_id) -> <a href="./src/mixpeek/types/collections/file_delete_response.py">object</a></code>
- <code title="get /collections/file/{file_id}/full">client.collections.files.<a href="./src/mixpeek/resources/collections/files.py">full</a>(file_id, \*\*<a href="src/mixpeek/types/collections/file_full_params.py">params</a>) -> <a href="./src/mixpeek/types/collections/groupedfiledata.py">Groupedfiledata</a></code>

# Tasks

Types:

```python
from mixpeek.types import Taskresponse, TaskDeleteResponse
```

Methods:

- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/mixpeek/resources/tasks.py">retrieve</a>(task_id) -> <a href="./src/mixpeek/types/taskresponse.py">Taskresponse</a></code>
- <code title="delete /tasks/{task_id}">client.tasks.<a href="./src/mixpeek/resources/tasks.py">delete</a>(task_id) -> <a href="./src/mixpeek/types/task_delete_response.py">object</a></code>
