# Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N

def simple_multiplier(n: int = 0) -> int:
    list = []
    count = 2

    while count <= n:
        if n % count == 0:
            list.append(count)
            n /= count
        else:
            count += 1
    return list


n = int(input('Введите натуральное число N: '))
print(simple_multiplier(n))