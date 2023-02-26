import math, random

print("Exercise 1\n")

while True:
    try:
        figure = int(input("Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг\n: "))
        if figure == 1 or figure == 2 or figure == 3:
            break
        else:
            print("Введите от 1 до 3")
    except ValueError:
        print("Неверное значение")

while True:
    if figure == 1:
        try:
            side_1 = int(input("Введите сторону a = "))
            side_2 = int(input("Введите сторону b = "))
            side_3 = int(input("Введите сторону c = "))
            if side_1 > 0 and side_2 > 0 and side_3 > 0:
                break
        except ValueError:
            print("Неверное значение")
    elif figure == 2:
        try:
            side_1 = int(input("Введите длину = "))
            side_2 = int(input("Введите ширину = "))
            if side_1 > 0 and side_2 > 0:
                break
        except ValueError:
            print("Неверное значение")
    else:
        try:
            side_1 = int(input("Введите радиус = "))
            if side_1 > 0:
                break
        except ValueError:
            print("Неверное значение")

if figure == 1:
    p = (side_1 + side_2 + side_3)/2
    s = p*(p-side_1)*(p-side_2)*(p-side_3)
    print("Площадь фигуры ", round(math.sqrt(s), 2))
elif figure == 2:
    print("Площадь фигуры ", side_1*side_2)
else:
    print("Площадь фигуры ", round(math.pi*side_1**2, 2))

print()
print("-"*40)
print()

print("Exercise 2\n")

matrix = []
element = 1
for y in range(3):
    new_row = []
    for x in range(4):
        new_row.append(element)
        element += 1
    matrix.append(new_row)

for row in matrix:
    for x in row:
        print(x, end="\t")
    print()

print()

for indx in range(len(matrix[0])):
    for row in matrix:
        print(row[indx], end="\t")
    print()

print()
print("-"*40)
print()

print("Exercise 3\n")

matrix = [[random.randrange(0, 10) for x in range(6)] for y in range(6)]

for row in matrix:
    for x in row:
        print(x, end="\t")
    print()

some_list = [random.randrange(0, 10) for x in range(6)]
print(some_list)

for indx in range(len(matrix)):
    if indx % 2 != 1:
        matrix[indx] = some_list

print()

for row in matrix:
    for x in row:
        print(x, end="\t")
    print()

print()
print("-"*40)
print()

print("Exercise 4\n")

matrix = [[random.randrange(0, 10) for x in range(6)] for y in range(6)]

for row in matrix:
    for x in row:
        print(x, end="\t")
    print()

for indx in range(len(matrix)):
    if indx % 2 != 1:
        c = matrix[indx]
    else:
        matrix[indx-1] = matrix[indx]
        matrix[indx] = c

print()

for row in matrix:
    for x in row:
        print(x, end="\t")
    print()
