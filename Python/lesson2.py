n = int(input("Введите количество копеек: "))
if 1 <= n <= 99:
    print(n, end=" ")
    if n % 10 == 1 and n != 11:
        print("копейка")
    elif 2 <= n <= 4 or 2 <= n % 10 <= 4 and n > 20:
        print("копейки")
    else:
        print("копеек")
else:
    print("Некорректное значение")