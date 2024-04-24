from selenium import webdriver
from UntitledTestSuite.fixture.session import SessionHelper
from UntitledTestSuite.fixture.group import GroupHelper
class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_hame_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
