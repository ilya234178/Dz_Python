# Задайте список из k чисел последовательности (1 + 1\k)^k
# и выведите на экран их сумму.

# Было:
k = int(input('Введите число: '))
sum = 0

for i in range(1, k + 1):
    sum += (1 + 1 / i) ** i

print(f'Сумма списка из {k} чисел последовательности (1 + 1 \ k) ^ k равна: {sum}')

# Cтало:
from functools import reduce

k = int(input('Введите число: '))


def summa(k):
    lst = [(1 + 1 / i) ** i for i in range(1, k + 1)]
    sum = reduce(lambda x, y: x + y, lst)
    return sum


print(summa(k))