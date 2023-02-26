print("\nЗадание 1")

str1 = "I am learning Python. hello, WORLD!"
print("Изначальная строка:", str1)
print(str1[:str1.find("h")] + str1[str1.rfind("h") + 1:])


print("\nЗадание 2")
print("Изначальная строка:", str1)
print(str1[:str1.find("h")] + str1[str1.rfind("h")-1:str1.find("h"):-1] + str1[str1.rfind("h") + 1:])


print("\nЗадание 3")

str1 = input("Введите строку: ")
to_replace = input("Заменяемая подстрока: ")
replace = input("Новая подстрока: ")

print(str1.replace(to_replace, replace))


print("\nЗадание 4")

str1 = "Ежевику для ежат\nПринесли два ежа\nЕжевику еле-еле\nЕжата возле ели съели."
print(str1)
str2 = str1.replace("\n", " ").split(" ")
count = 0
for i in str2:
    if i[0] == "е" or i[0] == "Е":
        count += 1
print("Количество слов, начинающихся с 'е' =", count)
