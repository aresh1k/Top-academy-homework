def add_film(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap
    return wrapper


class UserInterface:
    @add_film('Ввод пользовательских данных')
    def wait_user_answer(self):
        print("Действия с фильмами:")
        print("1 - добавление фильма\n"
              "2 - каталог фильмов\n"
              "3 - просмотр определенного фильма\n"
              "4 - удаление фильма\n"
              "5 - узнать режиссера фильма\n"
              "6 - узнать длительность фильма\n"
              "q - выход из программы")
        user_answer = input("Выберите вариант действия:")
        return user_answer

    @add_film("Добавление фильма")
    def add_user_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссер": None,
            "год": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма")
        return dict_film

    @add_film("Каталог фильмов")
    def show_all_films(self, films):
        for ind, film in enumerate(films, start=1):
            print(f"{ind}. {film}")

    @add_film('Ввод названия фильма')
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_film('Просмотр фильма')
    def show_single_film(self, film):
        for key in film:
            print(f"{key} статьи - {film[key]}")

    @add_film('Сообщение об ошибке')
    def show_incorrect_error(self, user_film):
        print(f"Фильма с названием {user_film} не существует")

    @add_film('Удаление фильма')
    def remove_single_film(self, film):
        print(f"Фильм {film} - был удален")

    @add_film("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Варианта {answer} не существует")

    @add_film("Узнать режиссера фильма")
    def show_film_producer(self, producer):
        print(f"Режиссер указанного фильма - {producer}")

    @add_film("Узнать длительность фильма")
    def show_film_duration(self, duration):
        print(f"Длительность указанного фильма - {duration}")
