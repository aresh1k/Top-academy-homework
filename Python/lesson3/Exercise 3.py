print("Программа для нахождения максимального значения из трех введенных значений")

while True:
    try:
        first = int(input("Введите первое значение: "))
        break
    except ValueError:
        print("Неверное значение")

while True:
    try:
        second = int(input("Введите второе значение: "))
        break
    except ValueError:
        print("Неверное значение")

while True:
    try:
        third = int(input("Введите третье значение: "))
        break
    except ValueError:
        print("Неверное значение")

print("Максимальное значение: ", first if first > second and first > third else second if second > third else third)