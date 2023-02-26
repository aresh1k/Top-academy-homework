from random import randrange

print("Задание №1")

amount = int(input("Введите количество чисел: "))
numbers = [randrange(-100, 100) for i in range(amount)]
print(numbers)
numb = 0
for i in numbers:
    if i % 13 == 0 and i > 0:
        if i > numb:
            numb = i
if numb != 0:
    print("Наибольшее положительное кратное 13 число:", numb)
else:
    print("Положительного кратного 13 числа в списке нет")

print("\nЗадание №2")

some_tuple = ("ab", "abcd", "cde", "abc", "def")
print(some_tuple)
string = input("Введите значение: ")
status = False
for i in some_tuple:
    if string in i:
        status = True
        print(string, "есть в кортеже.")
        break
if status == False:
    print(string, "отсутствует в кортеже.")

print("\nЗадание №3")

some_tuple = (input("Введите по порядку, без пробелов, элементы кортежа: "))
some_list = []
for i in some_tuple:
    amount = 0
    if i not in some_list:
        some_list.append(i)
    else:
        continue
    for j in some_tuple:
        if i == j:
            amount += 1
    print("\nКоличество", i, "=", amount)
