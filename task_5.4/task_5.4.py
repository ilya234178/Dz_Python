# Даны два файла, в каждом из которых находится запись многочлена.
#  Задача - сформировать файл, содержащий сумму многочленов
import random
def write_file(str):
    with open('file2.txt', 'a') as f:
        f.write(f'{str} \n')

def create_coeff(k):
    lst = [random.randint(0, 100) for i in range(k + 1)]
    return lst 
def create_coeff2(k2):
    lst2 = [random.randint(0, 100) for i in range(k2 + 1)]
    return lst2 

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
def create_polinom2(lst2):
    polinom2 = ''
    if len(lst2) < 1:
        polinom2 = 'x = 0'
    else:
        for i in range(len(lst2)):
            if i != len(lst2) - 1 and lst2[i] != 0 and i != len(lst2) - 2:
                polinom2 += f'{lst2[i]}x^{len(lst2) - i - 1}'
                if lst2[i + 1] != 0:
                    polinom2 += ' + '
            elif i == len(lst2) - 2 and lst2[i] != 0:
                polinom2 += f'{lst2[i]}x'
                if lst2[i + 1] != 0:
                    polinom2 += ' + '
            elif i == len(lst2) - 1 and lst2[i] != 0:
                polinom2 += f'{lst2[i]} = 0'
            elif i == len(lst2) - 1 and lst2[i] == 0:
                polinom2 += ' = 0'
    return polinom2

def sum_create_polinom(polinom, polinom2):
    sum_polinom = polinom + polinom2
    return sum_polinom

k = int(input("Введите натуральную степень k: "))
k2 = int(input("Введите натуральную степень k2: "))
write_file(create_polinom(create_coeff(k)))
write_file(create_polinom2(create_coeff2(k2)))
write_file(sum_create_polinom)


# я написал 5 задачу на основе 4 но не получилось сделать сложение.
#  Как профи подскажите в комментарии , как мне улучшить код и сделать сложение .
#  я надеюсь на вашу помощь))
