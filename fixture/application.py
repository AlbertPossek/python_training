from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/php4dvd/")

    def set_username_password(self, username, password):
        wd = self.wd
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        # Select checkbox "remember me"
        wd.find_element_by_id("rememberme").click()  # select the checkbox remember me
        # Check checkbox "remember me and print "Checkbox checked" in case it checked, or "Checkbox uchecked"  if it unchecked
        if wd.find_element_by_id("rememberme").is_selected():
            print("Checkbox checked")
        wd.find_element_by_xpath("//div[@class='col-xs-4']//button[.='Log in']").click()

    def dont_know_what_is_this(self):
        wd = self.wd
        # Don't understand what is this and why tests failed without this line
        ActionChains(wd).move_to_element(wd.find_element_by_xpath("//header[@class='main-header']/nav/div[3]/ul/li[1]/a")).perform()

    def click_on_settings_icon(self):
        wd = self.wd
        wd.find_element_by_css_selector("a.dropdown-toggle").click()

    def click_on_logout_option(self):
        wd = self.wd
        wd.find_element_by_link_text("Log out").click()

    def fill_movie_details(self, film):
        wd = self.wd
        wd.find_element_by_id("imdbid").click()
        wd.find_element_by_id("imdbid").clear()
        wd.find_element_by_id("imdbid").send_keys(film.imdbid)
        wd.find_element_by_id("name").click()
        wd.find_element_by_id("name").clear()
        wd.find_element_by_id("name").send_keys(film.title)
        wd.find_element_by_id("aka").click()
        wd.find_element_by_id("aka").clear()
        wd.find_element_by_id("aka").send_keys(film.known_as)
        wd.find_element_by_id("year").click()
        wd.find_element_by_id("year").clear()
        wd.find_element_by_id("year").send_keys(film.year)
        wd.find_element_by_id("duration").click()
        wd.find_element_by_id("duration").clear()
        wd.find_element_by_id("duration").send_keys(film.duration)
        wd.find_element_by_id("rating").click()
        wd.find_element_by_id("rating").clear()
        wd.find_element_by_id("rating").send_keys(film.rating)
        wd.find_element_by_id("format").click()
        wd.find_element_by_id("format").clear()
        wd.find_element_by_id("format").send_keys(film.format)
        wd.find_element_by_id("own_no").click()
        wd.find_element_by_id("seen_no").click()
        wd.find_element_by_id("loaned_no").click()
        wd.find_element_by_id("submit").click()

    def click_on_add_movie(self):
        wd = self.wd
        wd.find_element_by_link_text("Add movie").click()

    def destroy(self):
        self.wd.quit()
