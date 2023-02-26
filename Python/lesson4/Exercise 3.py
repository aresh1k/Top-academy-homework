some_list = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
number = 0
for i in some_list:
    amount = 0
    number = i
    for j in some_list:
        if i == j:
            amount += 1
    if amount == 1:
        print(i, end=" ")
        