# Напишите программу , которая по заданному номеру четверти ,
#  показывает диапазон возможных координат точек этой четверти(x и y)


from calendar import c
from pickletools import int4


i = int(input(f'Введите четверть : '))
if i > 4:
    print('Мы же договорились , что ты введешь цифры от 1 до 4')
if i == 1:
    print('x > 0 , y > 0')
if i == 2:
    print('x < 0 , y > 0')
if i == 3:
    print('x > 0 , y < 0')
if i == 4:
    print('x < 0 , y < 0')
