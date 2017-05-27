# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.film import Film


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

#****************** Login Test with empty username and password ***************
def test_login_empty(app):
    success = True
    app.open_home_page()
    app.set_username_password(username="", password="")
  #  app.assertTrue(success)

# ****************** Login Test with valid username and password ***************
def test_login_valid(app):
    success = True
    app.open_home_page()
    app.set_username_password(username="admin", password="admin")
 #   assertTrue(success)

# ****************** Add movie ***************
def test_add_new_movie(app):
    success = True
    app.open_home_page()
    app.set_username_password(username="admin", password="admin")
    app.dont_know_what_is_this()
    app.click_on_add_movie()
    app.fill_movie_details(Film(imdbid="10", title="My_Film1", year="1990", duration="94", rating="100", format="strange format", known_as="Also known as brbrbr"))
#    assertTrue(success)
