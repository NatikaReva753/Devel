from Test1.model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="test", firstname="Nata",
                                           homephone=1234, workphone=2345, mobilephone=3456,
                                           email_1="Nata@test.ru", email_2="Nata2@test.ru", email_3="Nata3@test.ru",
                                           day="17", month="May", year="2024", address="Moscow"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts