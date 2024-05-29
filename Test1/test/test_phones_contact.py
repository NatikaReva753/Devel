import re
from Test1.model.contact import Contact

def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="test", firstname="Nata",
                      homephone=1234, workphone=2345, mobilephone=3456,
                      email_1="Nata@test.ru", email_2="Nata2@test.ru", email_3="Nata3@test.ru",
                      day="17", month="May", year="2024", address="Moscow"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="test", firstname="Nata",
                      homephone=1234, workphone=2345, mobilephone=3456,
                      email_1="Nata@test.ru", email_2="Nata2@test.ru", email_3="Nata3@test.ru",
                      day="17", month="May", year="2024", address="Moscow"))
    contact_from_view_page = app.contact.get_contact_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone

def clear(s):
    #замена лишних символов, в 1 параметре передаем, что заменить, во 2 на что, 3 - откуда
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.homephone, contact.mobilephone, contact.workphone]))))