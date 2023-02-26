list1 = [5, 9, 6, 7]
list2 = [3, 11, 8]
list3 = [2, 4]
list4 = [10, 1, 12]

sort_type = input("Выберите сортировку:\n1 - сортировка по убыванию\n2 - сортировка по возрастанию\n")

def quick_sort(a):
    if len(a) > 1:
        x = a[(len(a) - 1) // 2]


        low = [i for i in a if i < x]
        eq = [i for i in a if i == x]
        hi = [i for i in a if i > x]
        if sort_type == "2":
            a = quick_sort(low) + eq + quick_sort(hi)
        else:
            a = quick_sort(hi) + eq + quick_sort(low)

    return a

new_list = quick_sort(list1+list2+list3+list4)

print(new_list)

find_number = int(input("Выберите значение для поиска: "))

def seq_search(s, item):

    for i in s:
        if i == item:
            return f"Значение {find_number} найдено"
    return f"Значение {find_number} не найдено"

print(seq_search(new_list, find_number))
