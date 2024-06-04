from Test.model.contact import Contact
import random



def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(lastname="", firstname="", homephone="", workphone="", mobilephone="",
                                           email_1="", email_2="", email_3="",
                                           day="", month="", year="", address=""
                                           ))
    old_contacts = db.get_contact_list()
    modified_contact = random.choice(old_contacts)
    contact = Contact(lastname="test", firstname="Nata",
                      homephone=1234, workphone=2345, mobilephone=3456,
                      email_1="Nata@test.ru", email_2="Nata2@test.ru", email_3="Nata3@test.ru",
                      day="17", month="May", year="2024", address="Moscow")
    contact.id = modified_contact.id
    app.contact.edit_contact_by_id(modified_contact.id, contact)
    new_contacts = db.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)

#def test_edit_first_contact_two(app):
    #if app.contact.count() == 0:
        #app.contact.create_contact(Contact(work=""))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.edit_first_contact(Contact(work="test"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

