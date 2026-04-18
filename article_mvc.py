class ArticleModel:
    def __init__(self, title, author, char_count, website, pub_date, description):
        self.title = title
        self.author = author
        self.char_count = char_count
        self.website = website
        self.pub_date = pub_date
        self.description = description

    def get_info(self):
        return {
            "заголовок": self.title,
            "автор": self.author,
            "Количество знаков": self.char_count,
            "Сайт публикации": self.website,
            "Дата публикации": self.pub_date,
            "Краткое описание": self.description
        }


class ArticleView:
    def display_article(self, article_data):
        print("\n--_ информация о статье ---")
        for key, value in article_data.items():
            print(f"{key}: {value}")
        print("---------------------------")


class ArticleController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        article_info = self.model.get_info()
        self.view.display_article(article_info)

# ЗАПУСК
if __name__ == "__main__":
    my_article = ArticleModel(
        title="как выучить Python за 30 дней",
        author="Иван Иванович",
        char_count=5230,
        website="КрутоБлог.ру",
        pub_date="15.03.2026",
        description="краткий гайд для новичков по быстрому освоению основ Python."
    )
    article_view = ArticleView()
    article_controller = ArticleController(my_article, article_view)
    article_controller.update_view()