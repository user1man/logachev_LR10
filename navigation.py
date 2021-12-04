from math import cos, pi, sin


def start_menu():
    global state
    state = 'MENU'
    print('Выберите функцию')
    print('1. Решить функцию 1.t -- 1')


def func_menu():
    global state
    state = 'FUNC'
    print('Выберите действие')
    print('1. назад -- back')


def func_1():
    x = int(input('Введите x: '))
    y = int(input('Введите y: '))
    z = int(input('Введите z: '))
    numerator_1 = 2 * cos(x - pi/6)
    denominator_1 = 0.5 + sin(y) ** 2
    numerator_2 = z ** 2
    denominator_2 = 3 - (numerator_2 / 5)
    multiplier_1 = numerator_1 / denominator_2
    multiplier_2 = 1 + (numerator_2 / denominator_2)
    print('Ответ:', multiplier_1 * multiplier_2)


state = ''
start_menu()
while True:
    command = input('Команда: ')
    if state == "MENU":
        if command == '1':
            func_1()
            func_menu()
        else:
            print('!!!Неверная команда!!!')
            start_menu()
    elif state == 'FUNC':
        if command == 'back':
            start_menu()
        else:
            print('!!!Неверная команда!!!')
            func_menu()