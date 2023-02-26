while True:
    operation = input("Введите операцию\n1 - 'r' - применение унарного минуса к операнду\n2 - '+' - сложение\n3 - '-' - вычитание\n4 - '/' - деление\n5 - '*' - умножение\n6 - '%' - остаток от деления\n7 - '<' - минимальное из двух чисел\n8 - '>' - максимальное из двух чисел\n")
    if operation == "r" or operation == "+" or operation == "-" or operation == "/" or operation == "*" or operation == "%" or operation == "<" or operation == ">":
        break
    else:
        print("Неверное значение")

if operation != "r":
    while True:
        try:
            first_number = int(input("Введите первое число: "))
            second_number = int(input("Введите второе число: "))
            if operation != "/" or operation != "%":
                if second_number != 0:
                    break
                else:
                    print("На ноль делить нельзя")
            else:    
                break
        except ValueError:
            print("Введено неверное значение")
else:
    while True:
        try:
            first_number = int(input("Введите первое число: "))
            break
        except ValueError:
            print("Введено неверное значение")

print()

if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "/":
    print(first_number / second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "%":
    print(first_number % second_number)
elif operation == "/":
    print(first_number / second_number)
elif operation == ">":
    print(first_number if first_number > second_number else second_number)
elif operation == "<":
    print(first_number if first_number < second_number else second_number)
else:
    first_number = -first_number
    print(first_number)