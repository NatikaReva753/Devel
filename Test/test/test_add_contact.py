from Test.fixture.application import Application
from Test.model.contact import Contact
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact("Nata", "UntitledTestSuite", "UntitledTestSuite", "UntitledTestSuite", "UntitledTestSuite"))
    app.session.logout()

def test_add_contact_two(app):
    app.session.login("admin", "secret")
    app.contact.create_contact(Contact("", "", "", "", ""))
    app.session.logout()