import pytest

from mysite.blog.views.post_views import PostView
from mysite.blog.tests.factories import PostFactory


@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'