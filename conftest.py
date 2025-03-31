import pytest

from endpoints.change_meme import ChangeMeme
from endpoints.create_new_meme import CreateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.endpoint import Endpoint
from endpoints.get_meme import GetMeme
from endpoints.get_memes import GetMemes


@pytest.fixture(scope="session")
def token():
    authorize_endpoint = Endpoint()
    yield authorize_endpoint.authorization()


@pytest.fixture()
def meme(token):
    body = {
        "text": "Jackie_Chan_WTF",
        "url": "https://www.einstein1.net/wp-content/uploads/2021/04/bedeutung-memes-what-is-that-thing.jpeg",
        "tags": ["actor", "WTF"],
        "info": {"format": "jpeg"}
    }
    new_meme = CreateMeme(token)
    new_meme.create_meme(payload=body)
    yield new_meme.response_formatted_to_json
    delete_meme = DeleteMeme(token)
    delete_meme.delete_meme(new_meme.response_formatted_to_json['id'])


@pytest.fixture()
def meme_id(meme):
    return meme["id"]

@pytest.fixture()
def get_memes_endpoint(token):
    return GetMemes(token)

@pytest.fixture()
def get_meme_endpoint(token):
    return GetMeme(token)

@pytest.fixture()
def create_meme_endpoint(token):
    return CreateMeme(token)

@pytest.fixture()
def change_meme_endpoint(token):
    return ChangeMeme(token)

@pytest.fixture()
def delete_meme_endpoint(token):
    return DeleteMeme(token)