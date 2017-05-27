class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
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

    def click_on_logout_option(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Log out").click()