# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

# Создание файла и запись в него
def write_file(str):
    with open('file.txt', 'w') as f:
        f.write(str)

# Создание случайных коэффициентов
def create_coeff(k):
    lst = [random.randint(0, 100) for i in range(k + 1)]
    return lst

# Создание многочлена
def create_polinom(lst):
    polinom = ''
    if len(lst) < 1:
        polinom = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                polinom += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    polinom += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                polinom += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    polinom += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                polinom += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                polinom += ' = 0'
    return polinom


k = int(input("Введите натуральную степень k: "))
write_file(create_polinom(create_coeff(k)))