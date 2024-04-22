# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact("Nata", "Test", "Test", "Test", "Test"))
    app.logout()

def test_add_contact_two(app):
    app.login("admin", "secret")
    app.create_contact(Contact("", "", "", "", ""))
    app.logout()

