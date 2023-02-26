while True:
    try:
        number = int(input("Загаданное число: "))
        if 0 < number < 101:
            break
        else:
            print("Введите загадываемое число от 1 до 100")
    except ValueError:
        pass

n = 1

while True:
    try:
        user_number = int(input("Введите число от 1 до 100: "))
        if 0 <= user_number < 101:
            if user_number == number:
                print("Вы угадалали загаданное число с", n, "раза")
                break
            elif user_number == 0:
                print("Вы отказались продолжать угадывать число")
                break
            else:
                print("Загаданное число больше" if user_number < number else "Загаданное число меньше")
                n += 1
    except ValueError:
        print("Неверное значение")