print("Задание 1")

some_dict = {
    "emp1": {"name": "Jhon", "salary": 7500},
    "emp2": {"name": "Emma", "salary": 8000},
    "emp3": {"name": "Brad", "salary": 6500},
}

print("До изменений", some_dict["emp3"])

some_dict["emp3"]["salary"] = 8500

print("После изменений", some_dict["emp3"])


print("Задание 2")

amount = int(input("Введите количество студентов: "))

some_dict = dict()

some_dict = {str(i) + "-й студент": {"first_name": input("Введите имя студента: "), "grade": int(input("Введите балл студента: "))} for i in range(1, amount+1)}

print(some_dict)

avg_grade = int(input("Введите средний балл: "))

print("Средний балл: ", avg_grade,". Студенты с баллом выше среднего:", sep="")

for value in some_dict:
    if some_dict[value]["grade"] > avg_grade:
        print(some_dict[value]["first_name"])
