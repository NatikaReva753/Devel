# -*- coding: utf-8 -*-
from Test.model.contact import Contact

def test_add_contact(app):
    app.session.login("admin", "secret", "secret")
    app.contact.mycontact(Contact("Nata", "test", "test", "test", "test", "test"))

def test_home_work_two(app):
    app.session.login("admin", "secret", "secret")
    app.contact.mycontact(Contact("", "", "", "", "", ""))
