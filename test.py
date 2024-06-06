from mixpeek import Mixpeek

mixpeek = Mixpeek("API_KEY")

# response = mixpeek.embed.video(
#     model="mixpeek/vuse-generic-v1",
#     input="https://mixpeek-public-demo.s3.us-east-2.amazonaws.com/media-analysis/Alien+Trailer+HD+(Original+1979+Ridley+Scott+Film)+Sigourney+Weaver.mp4",
#     input_type="url"
# )

# print(response)

response = mixpeek.tools.video.process(
    url="https://mixpeek-public-demo.s3.us-east-2.amazonaws.com/media-analysis/Alien+Trailer+HD+(Original+1979+Ridley+Scott+Film)+Sigourney+Weaver.mp4",
    frame_interval=5,
    resolution= [720, 1280],
    return_base64=True
)

print(response) # hi