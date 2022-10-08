# Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

def no_repeat(start_lst):
    final_lst = []

    for i in start_lst:
        if start_lst.count(i) == 1:
            final_lst.append(i)

    return final_lst


start_list = list(map(int, input('Введите список: ').split()))
print(no_repeat(start_list))