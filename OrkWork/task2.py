field = list(range(1,10))

def Print_field(field):
    print('=================')
    for i in range(3):
        print('|',field[0+i*3],'|','|',field[1+i*3],'|','|',field[2+i*3],'|')
    print('=================')

def check_win(field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False

def take_input(player):
    valid = False
    while not valid:
        player_step = (input(f'Выберите незанятое поле для установки знака {player} от 1 до 9: '))
        player_step = int(player_step)
        if 1 <= player_step <= 9:
            if str(field[player_step - 1]) not in 'OX':
                field[player_step - 1] = player
                valid = True
            else:
                print('Эта клетка уже занята!')
        else:
            print('Некорректный ввод. Введите число от 1 до 9')

def main(field):
    count = 0
    win = False
    while not win:
        Print_field(field)
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        count += 1
        result = check_win(field)
        if result:
            print(result, 'выиграл!')
            win = True
            break
        if count == 9:
            print('Ничья!')
            break
    Print_field(field)


main(field)