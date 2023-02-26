list1 = [2, 4, 6]
list2 = [5, 8, 2]
list3 = [1, 6, 8]

square = 0


def square_global(a, b, c):
    def get_square(lenght, width):
        return lenght*width

    global square
    square = 2 * (get_square(a, b)+get_square(a, c)+get_square(b, c))
    return square

print("Глобальная переменная")
square_global(*list1)
print(square)
square_global(*list2)
print(square)
square_global(*list3)
print(square)


def square_local(a, b, c):
    def get_square(lenght, width):
        return lenght*width

    square = 2 * (get_square(a, b)+get_square(a, c)+get_square(b, c))
    return square

print("Локальная переменная")
print(square_local(*list1))
print(square_local(*list2))
print(square_local(*list3))


def square_nonlocal(a, b, c):
    square = 0

    def get_square(lenght, width):
        nonlocal square
        s += lenght*width

    get_square(a, b)
    get_square(a, c)
    get_square(b, c)

    square = 2 * square
    return square

print("Нелокальная переменная")
print(square_local(*list1))
print(square_local(*list2))
print(square_local(*list3))
