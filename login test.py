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

class login test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_login test(self):
        success = True
        wd = self.wd
        wd.get("http://localhost:8080/php4dvd/")
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("root")
        wd.find_element_by_xpath("//div[@class='col-xs-4']//button[.='Log in']").click()
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("admin")
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("admin")
        wd.find_element_by_xpath("//div[@class='col-xs-4']//button[.='Log in']").click()
        wd.find_element_by_link_text("Add movie").click()
        wd.find_element_by_id("name").click()
        wd.find_element_by_id("name").clear()
        wd.find_element_by_id("name").send_keys("test1")
        wd.find_element_by_id("year").click()
        wd.find_element_by_id("year").clear()
        wd.find_element_by_id("year").send_keys("2001")
        wd.find_element_by_xpath("//label[@for='own_no']").click()
        if not wd.find_element_by_id("own_no").is_selected():
            wd.find_element_by_id("own_no").click()
        wd.find_element_by_id("submit").click()
        wd.find_element_by_css_selector("section.content").click()
        wd.find_element_by_css_selector("i.fa.fa-wrench").click()
        wd.find_element_by_link_text("Log out").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
