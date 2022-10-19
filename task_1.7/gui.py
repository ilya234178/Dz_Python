def add_contact():
    name = input('Введите имя контакта: ')
    about = input('Введите описание контакта: ')
    number = input('Введите номер контакта: ')
    col = name + ', ' + about + ', ' + number + ';'
    return col


def find_contact():
    name = input('Введите имя контакта: ')
    return name


def action():
    act = input('Введите действие: ')
    return act


def path_file():
    path = input('Введите путь: ')
    return path