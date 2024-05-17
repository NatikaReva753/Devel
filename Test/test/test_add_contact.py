from Test.model.contact import Contact



def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="test", firstname="Nata",
                      homephone=1234, workphone=2345, mobilephone=3456)
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_contact_two(app):
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact("", "", "", "", "")
    #app.contact.create_contact(contact)
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
