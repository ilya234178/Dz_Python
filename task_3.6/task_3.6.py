# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

# Было:
# number = input('Введите число: ')
# sum = 0

# for i in number:
#     if i != '.':
#         sum += int(i)

# print(f'Сумма равна: {sum}')


# Стало:
from functools import reduce

number = input('Введите число: ')


def summa(number):
    lst = [int(x) for x in number if x != '.']
    sum = reduce(lambda x, y: x + y, lst)
    return sum


print(summa(number))