

def test_delete_first_movie(app):
    app.session.login(username="admin", password="admin")
    app.film.select_movie(film_name="My_Film1")
    app.session.logout()