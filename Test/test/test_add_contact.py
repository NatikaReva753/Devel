from Test.model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(lastname="", firstname="", homephone="", workphone="", mobilephone="",
                    email_1="", email_2="", email_3="", address="")] + [
    Contact(lastname=random_string("lastname", 10), firstname=random_string("firstname", 20),
          homephone=random_string("homephone", 20), workphone=random_string("workphone", 20),
            mobilephone=random_string("mobilephone", 20), email_1=random_string("email_1", 20),
            email_2=random_string("email_2", 20), email_3=random_string("email_3", 20),
            address=random_string("address", 20))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

