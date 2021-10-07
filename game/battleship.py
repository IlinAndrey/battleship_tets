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


def get_row():
    while True:
        try:
            guess = int(input("Строка: "))
            if guess in range(1, row_size + 1):
                return guess - 1
            else:
                print("\nЭто число вне океана")
        except ValueError:
            print("\nВведите число")


def get_col():
    while True:
        try:
            guess = int(input("Столбец: "))
            if guess in range(1, col_size + 1):
                return guess - 1
            else:
                print("\nЭто число вне океана")
        except ValueError:
            print("\nВведите число")


class Ship:
    def __init__(self, size, orientation, location):
        self.size = size

        if orientation == 'horizontal' or orientation == 'vertical':
            self.orientation = orientation
        else:
            raise ValueError("значение только по горизонтали или по вертикали.")

        if orientation == 'horizontal':
            if location['row'] in range(row_size):
                self.coordinates = []
                for index in range(size):
                    if location['col'] + index in range(col_size):
                        self.coordinates.append({'row': location['row'], 'col': location['col'] + index})
                    else:
                        raise IndexError("Выходит из значений")
            else:
                raise IndexError("Выходит из значений")
        elif orientation == 'vertical':
            if location['col'] in range(col_size):
                self.coordinates = []
                for index in range(size):
                    if location['row'] + index in range(row_size):
                        self.coordinates.append({'row': location['row'] + index, 'col': location['col']})
                    else:
                        raise IndexError("Выходит из значений")
            else:
                raise IndexError("Выходит из значений")

        if self.filled():
            print_board(board)
            print(" ".join(str(coords) for coords in self.coordinates))
            raise IndexError("Корабль полностью занял пространство")
        else:
            self.fillBoard()

    def filled(self):
        for coords in self.coordinates:
            if board[coords['row']][coords['col']] == 1:
                return True
        return False

    def fillBoard(self):
        for coords in self.coordinates:
            board[coords['row']][coords['col']] = 1

    def contains(self, location):
        for coords in self.coordinates:
            if coords == location:
                return True
        return False

    def destroyed(self):
        for coords in self.coordinates:
            if board_display[coords['row']][coords['col']] == 'O':
                return False
            elif board_display[coords['row']][coords['col']] == '*':
                raise RuntimeError("неточно")
        return True