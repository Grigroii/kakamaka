from utils import get_posts_all, search_for_posts, get_posts_by_user, get_post_by_pk, get_comments_by_post_id
from main import get_posters, get_post, get_json_list, get_json_post
import pytest
import main


def test_get_post_all():
    assert type(get_posts_all()) == list, 'Неверный формат файла'


def test_get_comments():
    assert type(get_comments_by_post_id(1)) == list, 'Неверный формат файла'


def test_get_comments_mismatch():
    with pytest.raises(ValueError):
        get_post(100)


def test_search_for_posts():
    assert type(search_for_posts(query='красиво')) == list, 'Неверный формат для файла для search_for_posts'


def test_get_posts_by_user_name():
    real_user = 'leo'
    try:
        posts = get_posts_by_user(real_user)
        assert True, 'Ошибка для имени leo'
    except ValueError as e:
        assert False, e


def test_get_posts_by_user_name_type():
    real_user = 'leo'
    posts = get_posts_by_user(real_user)
    assert type(posts) == list, 'Wrong returned type'


def test_get_posts_by_user_name_mismatch():
    with pytest.raises(TypeError):
        get_posters(user_name='Jhsdaony')


def test_get_posts_by_pk_positive():
    try:
        posts = get_post_by_pk(1)
        assert True, "Ошибка для значения 1"
    except ValueError('Айди пользователя отсутсвует') as e:
        assert False, e


def test_get_posts_by_pk_mismatch():
    with pytest.raises(ValueError):
        get_post_by_pk(pk=50)
