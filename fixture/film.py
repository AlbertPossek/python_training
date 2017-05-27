

class FilmHelper:

    def __init__(self, app):
        self.app = app

    def fill_movie_details(self, film):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_link_text("Add movie").click()

    def select_movie(self, film_name):
        wd = self.app.wd
        wd.find_element_by_link_text(film_name).click();
        wd.find_element_by_xpath('//*[@title="Remove"]').click()
        wd.switch_to_alert().accept()