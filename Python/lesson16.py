import re

print("\nЗадание 1, проверка пароля")

# password = "['my-p@ssw0rd']"

password = input("Введите пароль: ")

reg = "[A-Za-z0-9@_-]{6,18}"

print(re.search(reg, password))

def func(a):
    if re.search(a, password):
        return "соответствует заданным условиям"
    else:
        return "не соответствует заданным условиям"

print("Пароль", password, func(reg))


print("\nЗадание 2, проверка даты")

str1 = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
reg = "\d{1, 2}/\d{1, 2}/\d{1, 4}"
print(re.findall(reg, str1))
