from random import randrange
import re
from model.contact import Contact


def test_checking_all_contact_field(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="test", firstname="Nata",
                                           homephone="1234", workphone="2345", mobilephone="3456", address="Moscow",
                                           email_1="Nata@test.ru", email_2="Nata2@test.ru", email_3="Nata3@test.ru"))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_all_contacts_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test", firstname="Nata",
                                   homephone="1234", workphone="2345", mobilephone="3456", address="Moscow",
                                   email_1="Nata@test.ru", email_2="Nata2@test.ru", email_3="Nata3@test.ru"))
    # получение списка контактов на главной
    contact_from_home_page = app.contact.get_contact_list()
    # получение списка контактов из БД
    contact_from_db = db.get_contact_list()
    contact_from_home_page = sorted(contact_from_home_page, key=Contact.id_or_max)
    contact_from_db = sorted(contact_from_db, key=Contact.id_or_max)
    assert len(contact_from_home_page) == len(contact_from_db)
    for i in range(len(contact_from_db)):
        assert contact_from_home_page[i].firstname == contact_from_db[i].firstname
        assert contact_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contact_from_home_page[i].address == contact_from_db[i].address
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db[i])

def clear(s):
    return re.sub("[({}) -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email_1, contact.email_2, contact.email_3])))