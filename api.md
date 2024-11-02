# Indexes

Types:

```python
from mixpeek.types import IndexUploadResponse, IndexURLResponse
```

Methods:

- <code title="post /index/upload">client.indexes.<a href="./src/mixpeek/resources/indexes.py">upload</a>(\*\*<a href="src/mixpeek/types/index_upload_params.py">params</a>) -> <a href="./src/mixpeek/types/index_upload_response.py">IndexUploadResponse</a></code>
- <code title="post /index/url">client.indexes.<a href="./src/mixpeek/resources/indexes.py">url</a>(\*\*<a href="src/mixpeek/types/index_url_params.py">params</a>) -> <a href="./src/mixpeek/types/index_url_response.py">IndexURLResponse</a></code>

# Collections

Types:

```python
from mixpeek.types import CollectionDeleteResponse
```

Methods:

- <code title="delete /collections/{collection_id}">client.collections.<a href="./src/mixpeek/resources/collections/collections.py">delete</a>(collection_id) -> <a href="./src/mixpeek/types/collection_delete_response.py">object</a></code>

# Tasks

Types:

```python
from mixpeek.types import TaskRetrieveResponse, TaskDeleteResponse
```

Methods:

- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/mixpeek/resources/tasks.py">retrieve</a>(task_id) -> <a href="./src/mixpeek/types/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="delete /tasks/{task_id}">client.tasks.<a href="./src/mixpeek/resources/tasks.py">delete</a>(task_id) -> <a href="./src/mixpeek/types/task_delete_response.py">object</a></code>
