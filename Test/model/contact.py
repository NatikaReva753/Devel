from sys import maxsize

class Contact:

    def __init__(self, lastname=None, firstname=None, nickname=None, address=None, work=None, id=None):
        self.lastname = lastname
        self.firstname = firstname
        self.nickname = nickname
        self.address = address
        self.work = work
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and (
                self.lastname is None or other.lastname is None or self.lastname == other.lastname) and
                (self.firstname is None or other.firstname is None or self.firstname == other.firstname))

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize