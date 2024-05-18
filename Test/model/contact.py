from sys import maxsize

class Contact:

    def __init__(self, lastname=None, firstname=None, id=None,
                 day=None, month=None, year=None, id_contact=None, nickname=None, address=None, work=None,
                 homephone=None, mobilephone=None, workphone=None, all_phones_from_home_page=None,
                 email_1=None, email_2=None, email_3=None, all_emails_from_home_page=None):
        self.lastname = lastname
        self.firstname = firstname
        self.nickname = nickname
        self.address = address
        self.work = work
        self.id = id
        self.day = day
        self.month = month
        self.year = year
        self.id_contact = id_contact
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
            and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize