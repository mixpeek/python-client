# Shared Types

```python
from mixpeek.types import FilterCondition, ModelPaginationResponse, SortOption, TaskResponse
```

# Accounts

Types:

```python
from mixpeek.types import AccountUpdateResponse, AccountListResponse
```

Methods:

- <code title="put /accounts/">client.accounts.<a href="./src/mixpeek/resources/accounts.py">update</a>(\*\*<a href="src/mixpeek/types/account_update_params.py">params</a>) -> <a href="./src/mixpeek/types/account_update_response.py">AccountUpdateResponse</a></code>
- <code title="get /accounts/">client.accounts.<a href="./src/mixpeek/resources/accounts.py">list</a>() -> <a href="./src/mixpeek/types/account_list_response.py">AccountListResponse</a></code>

# Features

Types:

```python
from mixpeek.types import Feature, FeatureListResponse, FeatureDeleteResponse
```

Methods:

- <code title="get /features/{feature_id}">client.features.<a href="./src/mixpeek/resources/features/features.py">retrieve</a>(feature_id, \*\*<a href="src/mixpeek/types/feature_retrieve_params.py">params</a>) -> <a href="./src/mixpeek/types/feature.py">Feature</a></code>
- <code title="put /features/{feature_id}">client.features.<a href="./src/mixpeek/resources/features/features.py">update</a>(feature_id, \*\*<a href="src/mixpeek/types/feature_update_params.py">params</a>) -> <a href="./src/mixpeek/types/feature.py">Feature</a></code>
- <code title="post /features">client.features.<a href="./src/mixpeek/resources/features/features.py">list</a>(\*\*<a href="src/mixpeek/types/feature_list_params.py">params</a>) -> <a href="./src/mixpeek/types/feature_list_response.py">FeatureListResponse</a></code>
- <code title="delete /features/{feature_id}">client.features.<a href="./src/mixpeek/resources/features/features.py">delete</a>(feature_id) -> <a href="./src/mixpeek/types/feature_delete_response.py">object</a></code>

# Index

Types:

```python
from mixpeek.types import IndexTextResponse
```

Methods:

- <code title="post /index/text">client.index.<a href="./src/mixpeek/resources/index/index.py">text</a>(\*\*<a href="src/mixpeek/types/index_text_params.py">params</a>) -> <a href="./src/mixpeek/types/index_text_response.py">IndexTextResponse</a></code>

## Videos

Types:

```python
from mixpeek.types.index import VideoURLResponse
```

Methods:

- <code title="post /index/videos/url">client.index.videos.<a href="./src/mixpeek/resources/index/videos.py">url</a>(\*\*<a href="src/mixpeek/types/index/video_url_params.py">params</a>) -> <a href="./src/mixpeek/types/index/video_url_response.py">VideoURLResponse</a></code>

## Images

Types:

```python
from mixpeek.types.index import ImageURLResponse
```

Methods:

- <code title="post /index/images/url">client.index.images.<a href="./src/mixpeek/resources/index/images.py">url</a>(\*\*<a href="src/mixpeek/types/index/image_url_params.py">params</a>) -> <a href="./src/mixpeek/types/index/image_url_response.py">ImageURLResponse</a></code>

# Entities

## Faces

Types:

```python
from mixpeek.types.entities import FaceResponse, FaceListResponse, FaceDeleteResponse
```

Methods:

- <code title="post /entities/faces">client.entities.faces.<a href="./src/mixpeek/resources/entities/faces.py">create</a>(\*\*<a href="src/mixpeek/types/entities/face_create_params.py">params</a>) -> <a href="./src/mixpeek/types/entities/face_response.py">FaceResponse</a></code>
- <code title="patch /entities/faces/{face_id}">client.entities.faces.<a href="./src/mixpeek/resources/entities/faces.py">update</a>(\*, path_face_id, \*\*<a href="src/mixpeek/types/entities/face_update_params.py">params</a>) -> <a href="./src/mixpeek/types/entities/face_response.py">FaceResponse</a></code>
- <code title="get /entities/faces/{collection_id}">client.entities.faces.<a href="./src/mixpeek/resources/entities/faces.py">list</a>(collection_id, \*\*<a href="src/mixpeek/types/entities/face_list_params.py">params</a>) -> <a href="./src/mixpeek/types/entities/face_list_response.py">FaceListResponse</a></code>
- <code title="delete /entities/faces/{face_id}">client.entities.faces.<a href="./src/mixpeek/resources/entities/faces.py">delete</a>(face_id) -> <a href="./src/mixpeek/types/entities/face_delete_response.py">object</a></code>

# Assets

Types:

```python
from mixpeek.types import (
    AssetResponse,
    GroupedAssetData,
    AssetCreateResponse,
    AssetUpdateResponse,
    AssetDeleteResponse,
    AssetSearchResponse,
)
```

Methods:

- <code title="post /assets">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">create</a>(\*\*<a href="src/mixpeek/types/asset_create_params.py">params</a>) -> <a href="./src/mixpeek/types/asset_create_response.py">object</a></code>
- <code title="get /assets/{asset_id}">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">retrieve</a>(asset_id, \*\*<a href="src/mixpeek/types/asset_retrieve_params.py">params</a>) -> <a href="./src/mixpeek/types/asset_response.py">AssetResponse</a></code>
- <code title="patch /assets/{asset_id}">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">update</a>(asset_id, \*\*<a href="src/mixpeek/types/asset_update_params.py">params</a>) -> <a href="./src/mixpeek/types/asset_update_response.py">AssetUpdateResponse</a></code>
- <code title="delete /assets/{asset_id}">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">delete</a>(asset_id) -> <a href="./src/mixpeek/types/asset_delete_response.py">object</a></code>
- <code title="post /assets/search">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">search</a>(\*\*<a href="src/mixpeek/types/asset_search_params.py">params</a>) -> <a href="./src/mixpeek/types/asset_search_response.py">AssetSearchResponse</a></code>

## Features

Methods:

- <code title="get /assets/{asset_id}/features">client.assets.features.<a href="./src/mixpeek/resources/assets/features.py">list</a>(asset_id, \*\*<a href="src/mixpeek/types/assets/feature_list_params.py">params</a>) -> <a href="./src/mixpeek/types/grouped_asset_data.py">GroupedAssetData</a></code>

# Collections

Types:

```python
from mixpeek.types import CollectionListResponse, CollectionDeleteResponse
```

Methods:

- <code title="get /collections">client.collections.<a href="./src/mixpeek/resources/collections.py">list</a>(\*\*<a href="src/mixpeek/types/collection_list_params.py">params</a>) -> <a href="./src/mixpeek/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="delete /collections/{collection_id}">client.collections.<a href="./src/mixpeek/resources/collections.py">delete</a>(collection_id) -> <a href="./src/mixpeek/types/collection_delete_response.py">object</a></code>

# Tasks

Types:

```python
from mixpeek.types import TaskDeleteResponse
```

Methods:

- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/mixpeek/resources/tasks.py">retrieve</a>(task_id) -> <a href="./src/mixpeek/types/shared/task_response.py">TaskResponse</a></code>
- <code title="delete /tasks/{task_id}">client.tasks.<a href="./src/mixpeek/resources/tasks.py">delete</a>(task_id) -> <a href="./src/mixpeek/types/task_delete_response.py">object</a></code>

# Healthcheck

Types:

```python
from mixpeek.types import HealthCheckResponse
```

Methods:

- <code title="get /healthcheck">client.healthcheck.<a href="./src/mixpeek/resources/healthcheck.py">retrieve</a>() -> <a href="./src/mixpeek/types/health_check_response.py">HealthCheckResponse</a></code>
