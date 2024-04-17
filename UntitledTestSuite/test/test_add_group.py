# -*- coding: utf-8 -*-
import pytest
from UntitledTestSuite.model.group import Group
from UntitledTestSuite.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()

    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login("admin", "secret")
    app.create_group(Group("New", "test", "test"))
    app.session.logout()

def test_add_group_two(app):
    app.session.login("admin", "secret")
    app.create_group(Group("", "", ""))
    app.session.logout()
