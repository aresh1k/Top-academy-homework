class ValidSide:
    def __set_name__(self, owner, side):
        self.__side = side

    def __get__(self, instance, owner):
        return instance.__dict__[self.__side]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"Значение {value} должно быть целым числом")
        elif value <= 0:
            raise ValueError(f"Значение {value} должно быть больше 0")
        instance.__dict__[self.__side] = value


class Trigon:
    a = ValidSide()
    b = ValidSide()
    c = ValidSide()
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Треугольник со сторонами ({self.a, self.b, self.c})"

    def valid_trigon(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print(f"Треугольник со сторонами ({self.a, self.b, self.c}) существует")
        else:
            print(f"Треугольник со сторонами ({self.a, self.b, self.c}) не существует")


trigon1 = Trigon(2, 5, 6)
trigon2 = Trigon(5, 2, 8)
trigon3 = Trigon(7, 3, 6)

trigon1.valid_trigon()
trigon2.valid_trigon()
trigon3.valid_trigon()
