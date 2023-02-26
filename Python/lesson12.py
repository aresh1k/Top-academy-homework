import math

print("\nЗадание 1")

print("Площадь круга", (lambda radius: math.pi*radius**2)(2))

print("Площадь прямоугольника", (lambda length, width: length*width)(13, 10))

print("Площадь трапеции", (lambda length, width, height: (length+width)*height/2)(7, 5, 3))

print("\nЗадание 2")

print("Произведение трех чисел", (lambda first_num, second_num, third_num: first_num*second_num*third_num)(2, 5, 5))

print("\nЗадание 3")

test = [{"name": "Jennifer", "final": "95"},
        {"name": "David", "final": "92"},
        {"name": "Nikolas", "final": "98"}]

print("До сортировки по убыванию", test)
print("После сортировки по убыванию", sorted(test, key=lambda item: item["final"], reverse=True))

# minimal = 100
# for i in test:
#     if test[i]["final"] < minimal:
#         minimal = test[i]["final"]
# maximum = 0
# for i in test:
#     if test[i]["final"] > maximum:
#         maximum = test[i]["final"]

print("Минимальная оценка студентов", min(test, key=lambda item: item["final"]))
print("Максимальная оценка студентов", max(test, key=lambda item: item["final"]))

print("\nЗадание 4")

some_list = [3, 6, 8, 9, 1, 2]
print(some_list, "->", list(map(lambda x: x*some_list.index(x)**3, some_list)))

print("\nЗадание 5")

some_list = [3, 5, 7, 3, 9, 5, 7, 2]
print("Изначальный список", some_list)
print("Возведение списка в квадрат", list(map(lambda x: x**2, some_list)))
print("Возведение списка в куб", list(map(lambda x: x**3, some_list)))
