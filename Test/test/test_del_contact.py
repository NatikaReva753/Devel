import random

from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(lastname="test", firstname="Nata",
                                           homephone=1234, workphone=2345, mobilephone=3456,
                                           email_1="Nata@test.ru", email_2="Nata2@test.ru", email_3="Nata3@test.ru",
                                           day="17", month="May", year="2024", address="Moscow"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)