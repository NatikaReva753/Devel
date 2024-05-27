from Test.model.contact import Contact
import random
import string

constant = [
    Contact(lastname="lastname1", firstname="firstname1", homephone="homephone1", workphone="workphone1",
            mobilephone="mobilephone1", email_1="email_11", email_2="email_21", email_3="email_31", address="address1"),
    Contact(lastname="lastname2", firstname="firstname2", homephone="homephone2", workphone="workphone2",
            mobilephone="mobilephone2", email_1="email_12", email_2="email_22", email_3="email_32", address="address2")
]

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