def game():
    print("Игрок_1 выберите сторону: О или Х (На английской раскладке)")
    available_side = ['o', 'x']
    player_1 = input().lower()
    player_2 = 0
    if player_1 in available_side:
        if player_1 == 'o':
            print("Игрок_2 будет играть за сторону Х")
            player_2 = 'x'
        else:
            print("Игрок_2 будет играть за сторону O")
            player_2 = 'o'
        return player_1, player_2
    else:
        print("Ошибка! Введите корректную сторону: О или Х")
        return game()
def pole(field):
    #field = ['-'] * 9
    print("  0 1 2")
    for row in range(3):
        print(row, end=" ")
        for col in range(3):
            index = row * 3 + col
            print(field[index], end=" ")
        print()
def make_move(field, row, col, player):
    index = row * 3 + col
    if index in range(0, 9) and field[index] == '-':
        field[index] = player
        return True
    else:
        print("Неверный ход. Поле уже занято или некорректные координаты.")
        return False

def check_winner(field, player):
    for i in range(3):
        if all(field[i * 3 + j] == player for j in range(3)) or \
           all(field[j * 3 + i] == player for j in range(3)):
            return True
        if all(field[i * 3 + i] == player for i in range(3)) or \
           all(field[i * 3 + (2 - i)] == player for i in range(3)):
            return True
    return False


player_1, player_2 = game()
if player_1 is not None:
    current_player = player_1
    field = ['-'] * 9
    pole(field)
    print(f'Ходит Игрок_{1 if current_player == player_1 else 2}. Введите координаты, куда хотите сходить (в формате [ряд, столбец]): ')

    while True:
        coordinates = input("Введите координаты (в формате ряд столбец, например, '0 1' через пробел): ")
        coordinates =coordinates.split()
        if len(coordinates) != 2:
            print("Некорректный формат. Введите два числа через пробел.")
            continue

        if not coordinates[0].isdigit() or not coordinates[1].isdigit():
            print("Введите числа.")
            continue

        row, col = map(int, coordinates)
        if row in range(0,3) and col in range(0,3):
            if make_move(field, row, col, current_player):
                pole(field)
                if check_winner(field, current_player):
                    print(f'Игрок_{1 if current_player == player_1 else 2} выиграл!')
                    break
                else:
                    current_player = player_2 if current_player == player_1 else player_1
                    print(
                        f'Ходит Игрок_{1 if current_player == player_1 else 2}. Введите координаты, куда хотите сходить (в формате [ряд, столбец]): ')
            else:
                print("Попробуйте еще раз.")
        else:
            print("Некорректные координаты. Введите числа от 0 до 2.")