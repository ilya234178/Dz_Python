# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibb(num):
    list_pos = [1, 1]
    list_neg = [0, 1]

    for i in range(num - 2):
        list_pos.append(list_pos[i] + list_pos[i + 1])
    for i in range(num - 1):
        list_neg.append(list_neg[i] - list_neg[i + 1])
        i += 1

    return list_neg[::-1] + list_pos


num = int(input('Введите число: '))
print(fibb(num))
