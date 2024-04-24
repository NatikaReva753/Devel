from application import Application
from contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact("Nata", "UntitledTestSuite", "UntitledTestSuite", "UntitledTestSuite", "UntitledTestSuite"))
    app.logout()

def test_add_contact_two(app):
    app.login("admin", "secret")
    app.create_contact(Contact("", "", "", "", ""))
    app.logout()