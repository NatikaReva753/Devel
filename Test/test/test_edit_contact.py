from Test.model.contact import Contact



def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(firstname="test"))
    app.contact.edit_first_contact(Contact(firstname=""))

def test_edit_first_contact_two(app):
    if app.contact.count() == 0:
        app.contact.create_contact(Contact(work=""))
    app.contact.edit_first_contact(Contact(work="test"))
