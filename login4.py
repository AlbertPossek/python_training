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
    
    def test_(self):
        success = True
        wd = self.wd
        tmp = True
        # Open home page
        wd.get("http://localhost:8080/php4dvd/")
        # Find username field, clear it and set value "admin"
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("admin")
        # Find password field, clear it and set value "admin"
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("admin")
        # Select chackbox "remember me"
        wd.find_element_by_id("rememberme").click()         #select the checkbox remember me
        # Check checkbox "remember me and print "Checkbox checked" in case it checked, or "Checkbox uchecked"  if it unchecked
        if wd.find_element_by_id("rememberme").is_selected():
            print ("Checkbox checked")
        else:
            print("Checkbox unchecked")
        # Click on "Logon button"
        wd.find_element_by_xpath("//div[@class='col-xs-4']//button[.='Log in']").click()
        # Don't understand what is this and why tests failed without this line
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//header[@class='main-header']/nav/div[3]/ul/li[1]/a")).perform()
        # Click on "Settings" icon
        wd.find_element_by_css_selector("a.dropdown-toggle").click()
        # Click on "Logout" option
        wd.find_element_by_link_text("Log out").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
