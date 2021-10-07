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