class Clock:
    DAY = 86400

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{h}:{m}:{s}"

    @staticmethod
    def get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)
    
    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec % other.sec)

    def __isub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        self.sec -= other.sec
        return Clock(self.sec)

    def __imul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        self.sec *= other.sec
        return Clock(self.sec)

    def __ifloordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        self.sec //= other.sec
        return Clock(self.sec)

    def __imod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        self.sec %= other.sec
        return Clock(self.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec == other.sec

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec < other.sec
    
    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec <= other.sec
    
    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec > other.sec
    
    def __gq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec >= other.sec


c1 = Clock(200)
c2 = Clock(100)
c4 = Clock(600)
if c1 == c2:
    print("Время равно")
else:
    print("Время разное")
print("c4:", c4.get_format_time())
print("c1:", c1.get_format_time())
print("c4 < c1", c4 < c1)
print("c4 <= c1", c4 <= c1)
print("c4 > c1", c4 > c1)
print("c4 > c1", c4 >= c1)
print("c4 - c1:", (c4 - c1).get_format_time())
print("c4 * c1:", (c4 * c1).get_format_time())
print("c4 // c1:", (c4 // c1).get_format_time())
print(r"c4 % c1:", (c4 % c1).get_format_time())
c4 -= c1
print("c4 -= c1:", c4.get_format_time())
c4 *= c1
print("c4 *= c1:", c4.get_format_time())
c4 //= c1
print("c4 //= c1:", c4.get_format_time())
c4 %= c1
print("c4 %= c1:", c4.get_format_time())
