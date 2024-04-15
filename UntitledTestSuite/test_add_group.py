# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from group import Group
from application import Application
import unittest, time, re


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("New", "test", "test"))
        self.app.logout()

    def test_add_group_two(self):
        self.app.login("admin", "secret")
        self.app.create_group(Group("", "", ""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()