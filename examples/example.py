#!/usr/bin/env -S rye run python

from mixpeek_sdk import MixpeekSDK

client = MixpeekSDK()
agentresponse = client.agent.create(
    prompt="prompt",
)
print(agentresponse.task_id)
