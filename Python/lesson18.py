some_list = [-2, 3, 8, -11, -4, 6]
print("Изначальный список:", some_list)

def negative_counter(list_to_count):
    if len(list_to_count) == 1:
        return 0
    negative = 0
    if list_to_count[0] < 0:
        negative = 1
    return negative + negative_counter(list_to_count[1:])

print(negative_counter(some_list))
