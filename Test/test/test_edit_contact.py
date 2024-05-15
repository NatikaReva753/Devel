from Test.model.contact import Contact
from random import randrange



def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="", firstname=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="test", firstname="Nata")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_first_contact_two(app):
    #if app.contact.count() == 0:
        #app.contact.create_contact(Contact(work=""))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.edit_first_contact(Contact(work="test"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

