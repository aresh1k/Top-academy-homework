class Car:

    def input_info(self, model, year, manufacturer, engine_power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def set_model(self):
        self.model = input("Введите новый тип модели: ")

    def get_model(self):
        return self.model

    def set_year(self):
        self.year = input("Введите год производства: ")

    def get_year(self):
        return self.year

    def set_manufacturer(self):
        self.manufacturer = input("Введите производителя: ")

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine_power(self):
        self.engine_power = input("Введите новую мощность: ") + " л.с."

    def get_engine_power(self):
        return self.engine_power

    def set_color(self):
        self.color = input("Введите новый цвет: ")

    def get_color(self):
        return self.color

    def set_price(self):
        self.price = input("Введите новую цену: ")

    def get_price(self):
        return self.price

    def show_info(self):
        print("Модель:", self.model, "\n", "Год", self.year, "\n", "Производитель:", self.manufacturer, "\n",
        "Мощность двигателя:", self.engine_power, "\n", "Цвет:", self.color, "\n", "Цена:", self.price)
    
    def change_data(self):
        data = input("Какие данные изменить, введите цифру:\n1 - модель\n2 - год\n3 - производитель\n4 - мощность двигателя\n5 - цвет\n6 - цена\n")
        if data == "1":
            self.set_model()
        elif data == "2":
            self.set_year()
        elif data == "3":
            self.set_manufacturer()
        elif data == "4":
            self.set_engine_power
        elif data == "5":
            self.set_color()
        elif data == "6":
            self.set_price()
        self.show_info()

BMW = Car()
BMW.input_info(model = "X7 M50i", year = 2021, manufacturer = "BMW", engine_power = "530 л.с.", color = "white", price = "10790000")
BMW.show_info()
BMW.change_data()
