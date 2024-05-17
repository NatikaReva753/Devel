from sys import maxsize

class Contact:

    def __init__(self, lastname=None, firstname=None, id=None, homephone=None, mobilephone=None, workphone=None,
                 nickname=None, address=None, work=None, all_phones_from_home_page=None):
        self.lastname = lastname
        self.firstname = firstname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.nickname = nickname
        self.address = address
        self.work = work
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id

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