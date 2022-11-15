# Числовая угадайка
import random


def is_valid(n):
    if n.isdigit():
        return True
    else:
        return False


def compare_numbers(n, comp_n):
    n = int(n)
    if n > comp_n:
        print('Ваше число больше загаданного, попробуйте ещё разок')
        return False
    elif n < comp_n:
        print('Ваше число меньше загаданного, попробуйте ещё разок')
        return False
    else:
        print('Вы угадали, поздравляем!')
        return True


def continue_game():
    cont = input('Может сыграем ещё разок?(да/нет)')
    while True:
        if cont.lower() == 'да':
            return True
        if cont.lower() == 'нет':
            return False
        else:
            cont = input('Введите да или нет')


def game():
    print("Добро пожаловать в числовую угадайку!\n В каком диапазоне чисел "
          "будем играть?")
    x, y = input('Введите от '), input(' до ')

    total_tries = 0

    while True:
        if is_valid(x) and is_valid(y) and int(x) < int(y):
            comp_num = random.randint(int(x), int(y))
            print('Супер! Компьютер загадал число, попробуй отгадать!')
            break
        else:
            print('Неверный диапазон')
            x, y = input('Введите целое число от \n'), input('Введите целое '
                                                             'число до \n')

    num = input('Твоё число?')

    while True:
        if is_valid(num) and int(x) <= int(num) <= int(y):
            total_tries += 1
            if compare_numbers(num, comp_num):
                print('Количество попыток', total_tries)
                if continue_game():
                    game()
                    break
                else:
                    print("Спасибо, что играли в числовую угадайку. До "
                          "новых встреч;)")
                    break
            else:
                num = input()
        else:
            num = input('Неверно введено число:( Попробуй ещё раз\n')


game()
