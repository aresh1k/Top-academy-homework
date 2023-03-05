import math

class Pair:

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def change_number(self, number, new_value):
        if number == "A":
            self.A = new_value
        else:
            self.B = new_value

    def summa(self):
        return self.A + self.B

    def multiplication(self):
        return self.A * self.B

class Right_Triangle(Pair):

    def __init__(self, A, B):
        super().__init__(A, B)

    def hypotenuse(self):
        return round(math.sqrt(self.A**2 + self.B**2), 2)

    def area(self):
        p = (super().summa() + self.hypotenuse())/2
        return round(math.sqrt(p*(p-self.A)*(p-self.B)*(p-self.hypotenuse())))

    def print_info(self):
        print()
        print("Гипотенуза ΔABC:", self.hypotenuse())
        print(f"Прямоугольный треугольник ΔABC {self.A}, {self.B}, {self.hypotenuse()}")
        print("Площадь ΔABC:", self.area())
        print("Сумма катетов =", super().summa())
        print("Произведение катетов =", super().multiplication())


triangle = Right_Triangle(5, 8)
triangle.print_info()
triangle.change_number("A", 6)
triangle.print_info()
