from Test.model.contact import Contact



def test_add_contact(app):
    app.contact.create_contact(Contact("Nata", "UntitledTestSuite", "UntitledTestSuite", "UntitledTestSuite", "UntitledTestSuite"))

def test_add_contact_two(app):
    app.contact.create_contact(Contact("", "", "", "", ""))