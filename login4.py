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
        wd.get("http://localhost:8080/php4dvd/")
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("html")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.content-wrapper")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.login-box-body")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("username")).perform()
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("admin")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("admin")
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.login-box-body")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.col-xs-4")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@class='col-xs-4']//button[.='Log in']")).perform()
      #  wd.find_element_by_id("password").click()
      #  wd.find_element_by_id("password").send_keys("\\undefined")
        wd.find_element_by_xpath("//div[@class='col-xs-4']//button[.='Log in']").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("section.content")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='movie_4']/div[1]/div")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_id("movie_4")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("nav.navbar.navbar-static-top")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//header[@class='main-header']/nav/div[3]/ul/li[1]/a")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("i.fa.fa-home")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//header[@class='main-header']/nav/div[3]/ul/li[1]/a")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("a.dropdown-toggle")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("i.fa.fa-wrench")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("a.dropdown-toggle")).perform()
        wd.find_element_by_css_selector("a.dropdown-toggle").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("i.fa.fa-wrench")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("User management")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("My profile")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_link_text("Log out")).perform()
        wd.find_element_by_link_text("Log out").click()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.content-wrapper")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("footer.main-footer")).perform()
        ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.content-wrapper")).perform()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
