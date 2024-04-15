# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login("admin", "secret")
    app.create_group(Group("New", "test", "test"))
    app.logout()

def test_add_group_two(app):
    app.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.logout()