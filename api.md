# Describe

Types:

```python
from mixpeek.types import DescribeUploadResponse, DescribeURLResponse
```

Methods:

- <code title="post /describe/upload">client.describe.<a href="./src/mixpeek/resources/describe.py">upload</a>(\*\*<a href="src/mixpeek/types/describe_upload_params.py">params</a>) -> <a href="./src/mixpeek/types/describe_upload_response.py">object</a></code>
- <code title="post /describe/url">client.describe.<a href="./src/mixpeek/resources/describe.py">url</a>(\*\*<a href="src/mixpeek/types/describe_url_params.py">params</a>) -> <a href="./src/mixpeek/types/describe_url_response.py">object</a></code>

# Indexes

Types:

```python
from mixpeek.types import IndexUploadResponse, IndexURLResponse
```

Methods:

- <code title="post /index/upload">client.indexes.<a href="./src/mixpeek/resources/indexes.py">upload</a>(\*\*<a href="src/mixpeek/types/index_upload_params.py">params</a>) -> <a href="./src/mixpeek/types/index_upload_response.py">IndexUploadResponse</a></code>
- <code title="post /index/url">client.indexes.<a href="./src/mixpeek/resources/indexes.py">url</a>(\*\*<a href="src/mixpeek/types/index_url_params.py">params</a>) -> <a href="./src/mixpeek/types/index_url_response.py">IndexURLResponse</a></code>

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
from mixpeek.types import CollectionListResponse, CollectionDeleteResponse
```

Methods:

- <code title="get /collections/">client.collections.<a href="./src/mixpeek/resources/collections/collections.py">list</a>() -> <a href="./src/mixpeek/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="delete /collections/{collection_id}">client.collections.<a href="./src/mixpeek/resources/collections/collections.py">delete</a>(collection_id) -> <a href="./src/mixpeek/types/collection_delete_response.py">object</a></code>

## Files

Types:

```python
from mixpeek.types.collections import Fileresponse, Groupedfiledata
```

# Tasks

Types:

```python
from mixpeek.types import TaskRetrieveResponse, TaskDeleteResponse
```

Methods:

- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/mixpeek/resources/tasks.py">retrieve</a>(task_id) -> <a href="./src/mixpeek/types/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="delete /tasks/{task_id}">client.tasks.<a href="./src/mixpeek/resources/tasks.py">delete</a>(task_id) -> <a href="./src/mixpeek/types/task_delete_response.py">object</a></code>
