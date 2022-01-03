from aocd import lines
from aocd import get_data
from aocd import submit

import re
import copy

get_data(day=4)

arr = []


def get_winning_board_index(marked_numbers):
    global arr
    index = -1

    arr2 = []
    for i, board in enumerate(boards):
        if (is_winning(board, marked_numbers)):
            index = i
            arr2 += [i]
    print(
        f"NEW: {str(list(set(arr2) - set(arr))).ljust(35)} LNP: {marked_numbers[-1]}")
    arr = arr2
    return (index, arr)


def is_winning(board, marked_numbers):
    for row in board:
        row_marked = True
        for num in row:
            if (num not in marked_numbers):
                row_marked = False
                break
        if (row_marked):
            return True

    for row in zip(*board):
        row_marked = True
        for num in row:
            if (num not in marked_numbers):
                row_marked = False
                break
        if (row_marked):
            return True
    return False


play = lines[0].split(",")

boards = []
new_board = []
for line in lines[2:]:

    if (line != ""):
        new_board.append(re.findall("\d+", line))

    if (len(new_board) == 5):
        boards.append(copy.deepcopy(new_board))
        new_board = []

#######################################################
won_board = 13
last_played_number = 80
marked_numbers = []
marked_numbers_copy = play[:play.index(str(last_played_number)) + 1]

for i in range(0, len(play)):
    marked_numbers = play[:i+1]
    get_winning_board_index(marked_numbers)
    # marked_numbers_copy = play[:i+1]
    # won_board = get_winning_board_index(marked_numbers)[0]
    # print(get_winning_board_index(marked_numbers)[1])
    # last_played_number = play[i]

sum = -1
if (won_board != -1):
    winnin_board = boards[13]
    sum = 0
    for row in winnin_board:
        for j in row:
            if (j not in marked_numbers_copy):
                sum += int(j)

print(
    f'sum: {sum}, won_board: {won_board}, last_played_number: {last_played_number}')

print(sum*int(last_played_number))
# submit(day=4, part='b', answer=sum*last_played_number)
