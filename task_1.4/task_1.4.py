# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math


def pi_fract(d):
    pi = str(math.pi)
    print(f'Число Пи: {pi}')
    return f'Число Пи с точностью {d} равно: {pi[0:len(d)]}'


d = str(input('Введите число: '))
print(pi_fract(d))