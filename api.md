# Shared Types

```python
from mixpeek.types import FilterCondition, ModelPaginationResponse, SortOption, TaskResponse
```

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

# Assets

Types:

```python
from mixpeek.types import (
    AssetResponse,
    GroupedAssetData,
    AssetCreateResponse,
    AssetDeleteResponse,
    AssetSearchResponse,
)
```

Methods:

- <code title="post /assets">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">create</a>(\*\*<a href="src/mixpeek/types/asset_create_params.py">params</a>) -> <a href="./src/mixpeek/types/asset_create_response.py">AssetCreateResponse</a></code>
- <code title="get /assets/{asset_id}">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">retrieve</a>(asset_id, \*\*<a href="src/mixpeek/types/asset_retrieve_params.py">params</a>) -> <a href="./src/mixpeek/types/asset_response.py">AssetResponse</a></code>
- <code title="patch /assets/{asset_id}">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">update</a>(asset_id, \*\*<a href="src/mixpeek/types/asset_update_params.py">params</a>) -> <a href="./src/mixpeek/types/asset_response.py">AssetResponse</a></code>
- <code title="delete /assets/{asset_id}">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">delete</a>(asset_id) -> <a href="./src/mixpeek/types/asset_delete_response.py">object</a></code>
- <code title="post /assets/search">client.assets.<a href="./src/mixpeek/resources/assets/assets.py">search</a>(\*\*<a href="src/mixpeek/types/asset_search_params.py">params</a>) -> <a href="./src/mixpeek/types/asset_search_response.py">AssetSearchResponse</a></code>

## Features

Methods:

- <code title="get /assets/{asset_id}/features">client.assets.features.<a href="./src/mixpeek/resources/assets/features.py">list</a>(asset_id, \*\*<a href="src/mixpeek/types/assets/feature_list_params.py">params</a>) -> <a href="./src/mixpeek/types/grouped_asset_data.py">GroupedAssetData</a></code>

# Collections

Types:

```python
from mixpeek.types import CollectionListResponse
```

Methods:

- <code title="get /collections">client.collections.<a href="./src/mixpeek/resources/collections.py">list</a>(\*\*<a href="src/mixpeek/types/collection_list_params.py">params</a>) -> <a href="./src/mixpeek/types/collection_list_response.py">CollectionListResponse</a></code>

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
