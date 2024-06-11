from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))