from Test.model.contact import Contact



def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(lastname="", firstname=""))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="test", firstname="Nata")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_first_contact_two(app):
    #if app.contact.count() == 0:
        #app.contact.create_contact(Contact(work=""))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.edit_first_contact(Contact(work="test"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

