#  Создайте программу для игры в ""Крестики-нолики"".


mas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]


# Вывод поля на экран
def print_mas():
    print(mas[0], end=" ")
    print(mas[1], end=" ")
    print(mas[2])

    print(mas[3], end=" ")
    print(mas[4], end=" ")
    print(mas[5])

    print(mas[6], end=" ")
    print(mas[7], end=" ")
    print(mas[8])


# Ход
def step_mas(step, p_sign):
    i = mas.index(step)
    mas[i] = p_sign


# Проверка выигрыша
def win():
    winner = ''
    for i in victory:
        if mas[i[0]] == 'X' and mas[i[1]] == 'X' and mas[i[2]] == 'X':
            winner = print(f'Победил {p_1}!')
        if mas[i[0]] == '0' and mas[i[1]] == '0' and mas[i[2]] == '0':
            winner = print(f'Победил {p_2}!')

    return winner


p_1 = input('Введите имя первого игрока: ')
p_2 = input('Введите имя второго игрока: ')
game_over = False
count = True

# Игра
while game_over == False:
    print_mas()

    if count:
        p_sign = 'X'
        step = int(input(f'Ходит {p_1}: '))
        count = False
    else:
        p_sign = '0'
        step = int(input(f'Ходит {p_2}: '))
        count = True

    step_mas(step, p_sign)
    winner = win()

    if winner == '':
        game_over = False
    else:
        game_over = True

print_mas()