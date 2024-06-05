import pymysql.cursors
from Test.model.group import Group
from Test.model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

        #autocommit=True - сбрасывается кэш после каждого запроса

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3"
                           " from addressbook where deprecated is Null")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list.append(Contact(Contact(id_contact=str(id), firstname=firstname,
                                                lastname=lastname, address=address,
                                                homephone=home, mobilephone=mobile,
                                                workphone=work, email_1=email,
                                                email_2=email2, email_3=email3)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
