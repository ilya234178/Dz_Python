# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def composition_pair(list):
    result_list = []
    j = -1

    for i in range(len(list) // 2):
        comp = list[i] * list[j]
        result_list.append(comp)
        j -= 1

    if len(list) % 2 != 0:
        print(result_list.append(list[(len(list) // 2)] ** 2))

    return result_list

print(composition_pair([2, 3, 4, 5, 6]))