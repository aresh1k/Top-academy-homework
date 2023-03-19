class Point3D:
    i = 1

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(f"Координаты {Point3D.i}-й точки: {self.x}, {self.y}, {self.z}")
        Point3D.i += 1

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return (self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        if other.x == 0 or other.y == 0 or other.z == 0:
            return "Делить на 0 нельзя"
        return (self.x / other.x, self.y / other.y, self.z / other.z)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False
    
    def __lt__(self, other):
        if self.x < other.x:
            print(f"x = {self.x} меньше x1 = {other.x}")
        else:
            print(f"x = {self.x} больше x1 = {other.x}")
        if self.y < other.y:
            print(f"y = {self.y} меньше y1 = {other.y}")
        else:
            print(f"y = {self.y} больше y1 = {other.y}")
        if self.z < other.z:
            print(f"z = {self.z} меньше z1 = {other.z}")
        else:
            print(f"z = {self.z} больше z1 = {other.z}")

    def __gt__(self, other):
        if self.x < other.x:
            print(f"x = {self.x} меньше x1 = {other.x}")
        else:
            print(f"x = {self.x} больше x1 = {other.x}")
        if self.y < other.y:
            print(f"y = {self.y} меньше y1 = {other.y}")
        else:
            print(f"y = {self.y} больше y1 = {other.y}")
        if self.z < other.z:
            print(f"z = {self.z} меньше z1 = {other.z}")
        else:
            print(f"z = {self.z} больше z1 = {other.z}")

    def change_coord(self, axis, value):
        if type(value) == int:
            if axis == "x":
                self.x = value
            elif axis == "y":
                self.y = value
            elif axis == "z":
                self.z = value
            else:
                return "Неверная координата"
            print(f"Запись значения в координату {axis}: {value}")
        else:
            return "Неверный тип значения"

point1 = Point3D(12, 15, 18)
point2 = Point3D(6, 3, 9)
print("Сложение координат:", point1 + point2)
print("Вычитание координат", point1 - point2)
print("Умножение координат", point1 * point2)
print("Деление координат", point1 / point2)
print("Равенство координат", point1 == point2)
point1 < point2
point1.change_coord("x", 20)
