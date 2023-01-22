import cohere
from api_keys import cohere_key

def get_youtube_videos(text_input):
    co = cohere.Client(f"{cohere_key}")
    response = co.generate(
                model="command-xlarge-nightly",
                text=f"Get 3 educational youtube videos about the following topic {text_input}"
            )
    return response.text

def get_articles(text_input):
    raise NotImplementedError


def get_mind_map_data(text_input):
    raise NotImplementedError
