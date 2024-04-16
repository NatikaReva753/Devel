# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_home_work(app):
    app.login("admin", "secret")
    app.crete_group(Group("Nata", "test", "test", "test", "test", "test"))
    app.Logout()

def test_home_work_two(app):
    app.login("admin", "secret")
    app.crete_group(Group("", "", "", "", "", ""))
    app.Logout()