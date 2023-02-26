while True:
    try:
        symbols_amount = int(input("Введите количество символов: "))
        if symbols_amount > 0:
            break
        else:
            print("Введите положительное число!")
    except ValueError:
        print("Неправильное значение!")

symbols_type = input("Введите тип символов: ")

print("Введите положительное число!")

while True:
    try:
        symbols_direction = int(input("Укажите направление символов\n0 - горизонтальное\n1 - вертикальное\nНаправление: "))
        if symbols_direction == 0 or symbols_direction == 1:
            break
        else:
            print("Введите 0 или 1!")
    except ValueError:
        print("Неправильное значение!")

if symbols_direction == 0:
    print(symbols_type*symbols_amount) 
else:
    i = 0
    while i < symbols_amount:
        print(symbols_type)
        i += 1