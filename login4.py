# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

import unittest
from film import Film
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class login4(unittest.TestCase):
    def setUp(self):
        self.app = Application()

#****************** Login Test with empty username and password ***************
    def test_login_empty(self):
        success = True
        self.app.open_home_page()
        self.app.set_username_password(username="", password="")
        self.assertTrue(success)

# ****************** Login Test with valid username and password ***************
    def test_login_valid(self):
        success = True
        self.app.open_home_page()
        self.app.set_username_password(username="admin", password="admin")
        self.assertTrue(success)

# ****************** Add movie ***************
    def test_add_new_movie(self):
        success = True
        self.app.open_home_page()
        self.app.set_username_password(username="admin", password="admin")
        self.app.dont_know_what_is_this()
        self.app.click_on_add_movie()
        self.app.fill_movie_details(Film(imdbid="10", title="My_Film1", year="1990", duration="94", rating="100", format="strange format", known_as="Also known as brbrbr"))
        self.assertTrue(success)

# ****************** Not tests ***************

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
