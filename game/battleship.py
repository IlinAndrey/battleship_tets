from random import randint
import os

row_size = 10  # кол-во строк
col_size = 10  # кол-во столбцов
num_ships = 4
max_ship_size = 4
min_ship_size = 1
num_turns = 40

ship_list = []
board = [[0] * col_size for x in range(row_size)]
board_display = [["O"] * col_size for x in range(row_size)]


def print_board(board_array):
    print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
    for r in range(row_size):
        print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
    print()


def search_locations(size, orientation):
    locations = []

    if orientation != 'horizontal' and orientation != 'vertical':
        raise ValueError("Ориентация должна иметь значение либо 'горизонтальная', либо 'вертикальная'.")

    if orientation == 'horizontal':
        if size <= col_size:
            for r in range(row_size):
                for c in range(col_size - size + 1):
                    if 1 not in board[r][c:c + size]:
                        locations.append({'row': r, 'col': c})
    elif orientation == 'vertical':
        if size <= row_size:
            for c in range(col_size):
                for r in range(row_size - size + 1):
                    if 1 not in [board[i][c] for i in range(r, r + size)]:
                        locations.append({'row': r, 'col': c})

    if not locations:
        return 'None'
    else:
        return locations


def random_location():
    size = randint(min_ship_size, max_ship_size)
    orientation = 'horizontal' if randint(0, 1) == 0 else 'vertical'

    locations = search_locations(size, orientation)
    if locations == 'None':
        return 'None'
    else:
        return {'позиция': locations[randint(0, len(locations) - 1)], 'размер': size, \
                'ориентация': orientation}
