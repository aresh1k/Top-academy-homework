import random

numbers = [random.randint(1, 10) for i in range(5, 10)]


def my_decorator(func):
    def average_sum(*args):
        return func(*args)/len(*args)
    
    return average_sum


@my_decorator
def summator(*args):
    summa = sum(*args)
    print("Сумма чисел", *numbers, "=", summa)
    return summa


print("Среднее арифметическое чисел", *numbers, "=", summator(numbers))
