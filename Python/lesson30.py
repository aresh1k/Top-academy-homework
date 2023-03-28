import json

some_dict = {
    "Turkey": "Ankara",
    "Egypt": "Cairo",
    "Spain": "Madrir",
    "Czech": "Prague"
}


class Capital:
    try:
        data = json.load(open("capital.json"))
    except FileNotFoundError:
        data = some_dict

        with open("capital.json", "w") as f:
            json.dump(data, f)

    @staticmethod
    def add_capital():
        country = input("Введите название страны для добавления (с заглавной буквы): ")
        city = input("Введите название столицы страны для добавления (с заглавной буквы): ")
        Capital.data[country] = city

        with open("capital.json", "w") as f:
            json.dump(Capital.data, f)

    @staticmethod
    def delete_capital():
        country = input("Введите название страны для удаления (с заглавной буквы): ")
        del Capital.data[country]

        with open("capital.json", "w") as f:
            json.dump(Capital.data, f)

    @staticmethod
    def find_capital():
        country = input("Введите название страны для поиска (с заглавной буквы): ")
        if country in Capital.data:
            print("Страна найдена в словаре")
        else:
            print("Страна не найдена в словаре")

    @staticmethod
    def change_data():
        while True:
            country = input("Введите название страны для добавления (с заглавной буквы): ")
            if country in Capital.data:
                break
            else:
                print("Указанной страны нет в словаре")
        city = input("Введите название столицы страны для добавления (с заглавной буквы): ")
        Capital.data[country] = city

        with open("capital.json", "w") as f:
            json.dump(Capital.data, f)

    @staticmethod
    def check_data():
        with open("capital.json") as f:
            print(json.load(f))


while True:
    user_input = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\n")
    if user_input == "1":
        Capital.add_capital()
    elif user_input == "2":
        Capital.delete_capital()
    elif user_input == "3":
        Capital.find_capital()
    elif user_input == "4":
        Capital.change_data()
    elif user_input == "5":
        Capital.check_data()
    elif user_input == "6":
        break
    else:
        print("Неверный ввод")
