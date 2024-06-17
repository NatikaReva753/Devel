from model.contact import Contact
from model.group import Group
import random

def test_del_contact_from_group(app, db, orm, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="Test",
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
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    contact = random.choice(contacts)
    del_group_from_contact = random.choice(groups)
    if len(orm.get_contacts_in_group(del_group_from_contact)) == 0:
        app.contact.add_contact_in_group_by_id(contact.id, del_group_from_contact.id)
    app.contact.del_contact_from_group_by_id(del_group_from_contact.id)
    new_contacts = orm.get_contact_list()
    list_contacts_not_in_group = orm.get_contacts_not_in_group(del_group_from_contact)
    assert contact in list_contacts_not_in_group
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)