# -*- coding: utf-8 -*-
from Test.model.group import Group
from Test.fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_home_work(app):
    app.session.login("admin", "secret")
    app.crete_group(Group("Nata", "test", "test", "test", "test", "test"))
    app.session.Logout()

def test_home_work_two(app):
    app.session.login("admin", "secret")
    app.crete_group(Group("", "", "", "", "", ""))
    app.session.Logout()