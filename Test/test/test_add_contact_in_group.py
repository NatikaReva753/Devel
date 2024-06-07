from Test.model.contact import Contact
from Test.model.group import Group
import random


def test_add_contact_in_group(app, orm, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test",
                                   middlename="Test",
                                   lastname="Test",
                                   nickname="test",
                                   title="title",
                                   company="Apple",
                                   address="Moscow",
                                   homephone="0000",
                                   mobilephone="1111",
                                   workphone="2221",
                                   fax="123456",
                                   email_1="Nata1@test.ru",
                                   email_2="Nata2@test.ru",
                                   email_3="Nata@test.ru",))
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    edit_contact = random.choice(contacts)
    add_group_to_contact = random.choice(groups)
    app.contact.add_contact_in_group_by_id(edit_contact.identifier, add_group_to_contact.identifier)
    new_contacts = orm.get_contact_list()
    list_contacts_in_group = orm.get_contacts_in_group(add_group_to_contact)
    assert edit_contact in list_contacts_in_group
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)