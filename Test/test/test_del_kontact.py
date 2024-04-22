
def test_delete_first_contact(app):
    app.session.login("admin", "secret", "secret")
    app.contact.delete_first_contact()
    app.session.Logout()
