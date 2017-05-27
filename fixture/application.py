from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.film import FilmHelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.film = FilmHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/php4dvd/")

    def destroy(self):
        self.wd.quit()
