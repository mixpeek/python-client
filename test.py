from mixpeek import Mixpeek
from pydantic import BaseModel

mixpeek = Mixpeek("")

response = mixpeek.embed.video(
    model_id="mixpeek/vuse-generic-v1",
    input="https://mixpeek-public-demo.s3.us-east-2.amazonaws.com/media-analysis/Alien+Trailer+HD+(Original+1979+Ridley+Scott+Film)+Sigourney+Weaver.mp4",
    input_type="url"
)

class ResponseFormat(BaseModel):
    city: int
    weather: float

generated_content = mixpeek.generate.text(
    model_id="openai/gpt-4-turbo",
    response_format=ResponseFormat,
    context="Please tell me the weather and make sure to respond in the provided JSON schema"
)



# print(response)

# response = mixpeek.tools.video.process(
#     url="https://mixpeek-public-demo.s3.us-east-2.amazonaws.com/media-analysis/Alien+Trailer+HD+(Original+1979+Ridley+Scott+Film)+Sigourney+Weaver.mp4",
#     frame_interval=5,
#     resolution= [720, 1280],
#     return_base64=True
# )

print(generated_content)