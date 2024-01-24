
ground = ['--', '--', '--', '--', '--', '--', '--', '--', '--', ]


def play_ground():
    print('     0  ', '  1  ', '  2 ')
    for i in range(3):
        print(i, ' ', ground[i * 3], '  ', ground[i * 3 + 1], '  ', ground[i * 3 + 2])


# Ходы Крестиков/Ноликов

def steps(symbol):
    while True:
        stp = input('Куда ставим: ' + symbol + '-ик, введите номер поля от 1 до 9\n'
                                               'где цифра соответствует координате поля\n'
                                               '0:0 - 1, 0:1 - 2, 0:2 - 3\n'
                                               '1:0 - 4, 1:1 - 5, 1:2 - 6\n'
                                               '2:0 - 7, 2:1 - 8, 2:2 - 9\n= ')
        if not (stp in '123456789'):
            print('Не верный ввод координаты поля, введити цифру от 1 до 9 ')
            play_ground()
            continue
        stp = int(stp)
        if str(ground[stp - 1]) in 'XO':
            print(f'Это поле уже занято, выберете другое')
            play_ground()
            continue
        ground[stp - 1] = symbol
        break


def chek_win():
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7,), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for i in wins:
        if ground[i[0]] == ground[i[1]] == ground[i[2]] != '--':
            return ground[i[1]]


# тело игры
def game():
    counter = 0
    while True:
        play_ground()
        if counter % 2 == 0:
            steps('X')
        else:
            steps('O')
        counter += 1
        winner = chek_win()
        if winner:
            print(f'Урра {winner}-ики,  победили!!!')
            break
        if counter > 8:
            print('Ну что ж, боевая НИЧЬЯ')
            break
    play_ground()
    print('До новых встреч!\nПриходите еще.')


game()
