from model.contact import Contact
from model.group import Group
import random

def test_del_contact_from_group(app, db, orm, check_ui):
    # Проверка наличия контакта, создание при необходимости
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
                                   email_3="Nata@test.ru"))
    # Проверка наличия группы, создание при необходимости
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    contacts = orm.get_contact_list()
    groups = orm.get_group_list()
    group = random.choice(groups)
    # Проверка есть ли контакт в группе
    contacts_in_group = orm.get_contacts_in_group(group)
    # Если группа пустая, добавляем в нее контакт
    if len(contacts_in_group) == 0:
        contact_to_add = random.choice(contacts)
        app.contact.add_contact_in_group_by_id(contact_to_add.id, group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    # Выбираем контакт из группы
    contact_to_delete = random.choice(contacts_in_group)
    # Удаляем выбранный контакт из группы
    app.contact.del_contacts_from_group(contact_to_delete.id, group.id)
    # Проверяем, что контакт был удален из группы
    list_contacts_not_in_group = orm.get_contacts_not_in_group(group)
    assert contact_to_delete in list_contacts_not_in_group
    if check_ui:
        new_contacts = orm.get_contact_list()
        assert sorted(app.contact.get_contact_list(), new_contacts, key=Contact.id_or_max)