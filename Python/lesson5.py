import random

print("Exercise 1\n")

some_list = [random.randint(0, 100) for i in range(10)]
print(some_list)
print("Max: ", max(some_list))
some_list.insert(0, some_list.pop(some_list.index(max(some_list))))
print(some_list)
print()
print('-' * 40)
print()


print("Exercise 2\n")

some_list = [random.randint(-99, 100) for i in range(10)]
print(some_list)
some_list.sort(reverse=True)
print(some_list)
print()
print('-' * 40)
print()


print("Exercise 3\n")

some_list = [random.randint(0, 100) for i in range(10)]
print(some_list)
print("Min: ", min(some_list))
print("Index min: ", some_list.index(min(some_list)))
for i in range(some_list.index(min(some_list))):
    some_list.pop(0)
print(some_list)