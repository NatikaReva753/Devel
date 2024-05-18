import re
from Test.model.contact import Contact

def test_email_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="test", firstname="Nata",
                                           homephone=1234, workphone=2345, mobilephone=3456,
                                           email_1="Nata@test.ru", email_2="Nata2@test.ru", email_3="Nata3@test.ru",
                                           day="17", month="May", year="2024", address="Moscow"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def clear(s):
    re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join([str(contact.email_1), str(contact.email_2), str(contact.email_3)])






