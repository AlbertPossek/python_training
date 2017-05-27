# -*- coding: utf-8 -*-
from model.film import Film


#****************** Login Test with empty username and password ***************
def test_login_empty(app):
    app.session.login(username="", password="")


# ****************** Login Test with valid username and password ***************
def test_login_valid(app):
    app.session.login(username="admin", password="admin")
    app.session.logout()


# ****************** Add movie ***************
def test_add_new_movie(app):
    app.session.login(username="admin", password="admin")
    app.film.click_on_add_movie()
    app.film.fill_movie_details(Film(imdbid="10", title="My_Film1", year="1990", duration="94", rating="100", format="strange format", known_as="Also known as brbrbr"))
  #  app.session.logout()       logout still doesn't work


