import pickle
import os


class Film:
    def __init__(self, title, genre, director, rental, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.rental = rental
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre})"


class FilmsModel:
    def __init__(self):
        self.film_name = "film.txt"
        self.films = self.load_data()

    def add_film(self, dict_films):
        film = Film(*dict_films.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_film = {
            "название фильма": film.title,
            "жанр": film.genre,
            "режиссер": film.director,
            "год выпуска": film.rental,
            "длительность": film.duration,
            "студия": film.studio,
            "актеры": film.actors
        }
        return dict_film

    def remove_film(self, user_title):
        return self.films.pop(user_title)

    def save_data(self):
        with open(self.film_name, "wb") as f:
            pickle.dump(self.films, f)

    def load_data(self):
        if os.path.exists(self.film_name):
            with open(self.film_name, "rb") as f:
                return pickle.load(f)

        else:
            return {}


