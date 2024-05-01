from Test.model.group import Group
from Test.fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.group.create(Group("New", "test", "test"))

def test_add_group_two(app):
    app.group.create(Group("", "", ""))