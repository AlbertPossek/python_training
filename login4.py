# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class login4(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/php4dvd/")

    def set_username_password(self, wd, username, password):
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)


    def select_checkbox(self, wd):
        # Select checkbox "remember me"
        wd.find_element_by_id("rememberme").click()  # select the checkbox remember me

    def print_checkbox_state(self, wd):
        # Check checkbox "remember me and print "Checkbox checked" in case it checked, or "Checkbox uchecked"  if it unchecked
        if wd.find_element_by_id("rememberme").is_selected():
            print("Checkbox checked")
        else:
            print("Checkbox unchecked")

    def click_login_button(self, wd):
        wd.find_element_by_xpath("//div[@class='col-xs-4']//button[.='Log in']").click()

    def dont_know_what_is_this(self, wd):
        # Don't understand what is this and why tests failed without this line
        ActionChains(wd).move_to_element(
            wd.find_element_by_xpath("//header[@class='main-header']/nav/div[3]/ul/li[1]/a")).perform()

    def click_on_settings_icon(self, wd):
        wd.find_element_by_css_selector("a.dropdown-toggle").click()

    def click_on_logout_option(self, wd):
        wd.find_element_by_link_text("Log out").click()

    def test_login_valid(self):
        success = True
        wd = self.wd
        tmp = True
        self.open_home_page(wd)
        self.set_username_password(wd, username="admin", password="admin")
        self.select_checkbox(wd)
        self.print_checkbox_state(wd)
        self.click_login_button(wd)
        self.dont_know_what_is_this(wd)
        self.click_on_settings_icon(wd)
        self.click_on_logout_option(wd)
        self.assertTrue(success)

    def test_login_empty(self):
        success = True
        wd = self.wd
        tmp = True
        self.open_home_page(wd)
        self.set_username_password(wd, username="", password="")
        self.select_checkbox(wd)
        self.print_checkbox_state(wd)
        self.click_login_button(wd)
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
