class MovieModel:
    def __init__(self, title, genre, director, release_year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.duration = duration
        self.studio = studio
        self.actors = actors
    def get_info(self):
        return {
            "Название": self.title,
            "Жанр": self.genre,
            "Режиссер": self.director,
            "год выпуска": self.release_year,
            "Длительность": f"{self.duration} мин.",
            "Студия": self.studio,
            "Актеры": self.actors
        }

class MovieView:
    def display_movie(self, movie_data):
        print("\n---- информация о фильме ----")
        for key, value in movie_data.items():
            if key == "актеры":
                print(f"{key}:")
                for actor_info in value:
                    print(f"  - {actor_info['ФИО']} (Роль: {actor_info['Роль']})")
            else:
                print(f"{key}: {value}")
        print("----------------------------------")

class MovieController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        movie_info = self.model.get_info()
        self.view.display_movie(movie_info)


if __name__ == "__main__":
    my_movie = MovieModel(
        title="Время приключений",
        genre="фантастика",
        director="Иван Иванович",
        release_year=2026,
        duration=120,
        studio="Киностудия Мечта",
        actors=[
            {"ФИО": "Петр Петрович", "Роль": "Главный герой"},
            {"ФИО": "Ольга Сидорова", "Роль": "Напарница"}
        ]
    )
    movie_view = MovieView()
    movie_controller = MovieController(my_movie, movie_view)
    movie_controller.update_view()