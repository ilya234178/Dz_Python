# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях

# Было:
# import random

# n = int(input('Введите число: '))
# list = []

# for i in range(n):
#     num = random.randint(-n, n)
#     list.append(num)
# print(list)

# a, b = map(int, input('Введите индексы двух элементов: ').split())
# print(f'Произведение элементов равно: {list[a] * list[b]}')


# Стало:
import random

n = int(input('Введите число: '))
lst = [random.randint(-n, n) for i in range(n)]
print(lst)
a, b = map(int, input('Введите индексы двух элементов: ').split())
print(f'Произведение элементов равно: {lst[a] * lst[b]}')