import pytest

from main import app
from utils import get_posts_all
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_api_posts(client):
    resp = client.get("/api/post")
    assert resp.status_code == 200
    assert type(resp.json) == list
    assert len(resp.json) > 0
    for item in resp.json:
        assert item.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
                               "pk", "is_bookmark"}


def test_api_post(client):
    resp = client.get("/api/post/1")
    assert resp.status_code == 200
    assert type(resp.json) == dict
    assert resp.json.keys() == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk",
                                "is_bookmark"}


def test_main():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "leo" in resp.get_data(True)


def test_has_error():
    with pytest.raises(ValueError):
        get_posts_all(file_name='asdasddata.json')
