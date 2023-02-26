numbers = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]

minimal = max(numbers)
maximum = 0

for i in numbers:
    simple = 0
    n = 1
    while n < i:
        if i % n == 0:
            simple += 1
        n += 1
    if simple == 1:
        if i < minimal:
            minimal = i
    else:
        if i > maximum:
            maximum = i

print("Минимальное простое число:", minimal)
print("Максимальное составное число:", maximum)
