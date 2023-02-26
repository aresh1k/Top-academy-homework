from random import randrange

print("\nЗадание 1")

first_list = ["red", "blue", "green"]
second_list = ["#FF0000", "#008000", "#0000FF"]
some_dict = dict(zip(first_list, second_list))

print(some_dict)

print("\nЗадание 2")

some_dict = {i: i**3 for i in range(1, 11)}
print(some_dict)

print("\nЗадание 3")

first_list = ["color", "fruit", "pet"]
second_list = ["blue", "apple", "dog"]
some_dict = {first_list[i]: second_list[i] for i in range(len(first_list))}
print(some_dict)

print("\nЗадание 4")

some_list = [randrange(0, 100) for i in range(randrange(1, 10))]

def min_value():
    return min(some_list)

print(some_list)

print(min_value())

print("\nЗадание 5")

some_list = [randrange(0, 10) for i in range(randrange(1, 6))]
new_list =[]

for i in range(len(some_list)):
    if i > 0:
        new_list.append(some_list[i-1]+some_list[i])
    else:
        new_list.append(some_list[i])

print("Изначальный список", some_list)
print("Измененный список", new_list)
