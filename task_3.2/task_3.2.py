# Задайте список из n чисел последовательности (1+ 1 / n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 2, 2: 2, 3: 2, 4:2, 5: 2, 6: 3} -> 13


n = int(input('Введите число: '))
sum = 0

for i in range(1, n + 1):
    sum += (1 + 1 / i) ** i

print(f'Сумма списка из {n} чисел последовательности (1 + 1 \ n) ** n равна: {round(sum)}')