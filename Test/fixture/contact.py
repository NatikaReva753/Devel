from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select
import random
class ContactHelper:
    def __init__(self, app):
        self.app = app
    def create_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # create contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[20]").click()
        self.return_to_contact_page()
        self.contact_cache = None
    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  address=address, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)
    def modify_first_contact(self):
        self.modify_contact_by_index(0)
    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # opening the contact edit form
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        # save the modified contact
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()
        self.contact_cache = None
    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # opening the contact edit form
        self.select_contact_by_id(id)
        self.fill_contact_form(contact)
        # save the modified contact
        wd.find_element_by_name("update").click()
        self.return_to_contact_page()
        self.contact_cache = None
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # opening the contact edit form
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
    #def select_contact_by_id(self, id):
     #   wd = self.app.wd
      #  wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
    #wd.find_elements_by_name("selected[]" % id).click()
    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()
    def get_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # читаем текст из поля
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, address=address, email=email, email2=email2, email3=email3)
    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone)
    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.return_to_contact_page()
        self.contact_cache = None

    def add_contact_in_group_by_id(self, id_contact, id_group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id_contact).click()
        Select(wd.find_element_by_xpath("//select[@name='to_group']")).select_by_value(id_group)
        wd.find_element_by_name("add").click()
        self.contact_cache = None

    def del_first_contact_from_group_by_id(self, id_group):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_xpath("//select[@name='group']")).select_by_value(id_group)
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("remove").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("title", contact.title)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("homepage", contact.homepage)
    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
    def return_to_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_value("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()
    def count_contacts(self):
        wd = self.app.wd
        self.app.open_home_page()
        # получение длины списка элементов
        return len(wd.find_elements_by_name("selected[]"))
