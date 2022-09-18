import numpy as np

def check_row(digit, row):
    if digit in board[row]:
        return False
    return True

def check_col(digit, col):
    if digit in board[:, col]:
        return False
    return True

def check_block(digit, row, col):
    block = (row // 3) * 3 + (col // 3)
    x = (block // 3) * 3
    y = (block % 3) * 3
    if digit in board[x:x+3, y:y+3]:
        return False
    return True

def print_board():
    n = 25
    for row in range(9):
        if row % 3 == 0:
            print('-' * n)
        for col in range(9):
            if col % 3 == 0:
                print('|', end=' ')
            digit = board[row, col]
            if digit == 0: digit = ' '
            print(digit, end=' ')
        print('|')
    print('-' * n)

def find_next_zero():
    for row in range(9):
        for col in range(9):
            if board[row, col] == 0:
                return row, col
    return -1, -1

def possible(digit, row, col):
    return all((check_row(digit, row), check_col(digit, col), check_block(digit, row, col)))

def solve():
    row, col = find_next_zero()
    if row == -1:
        print('\nSolution:')
        print_board()
        return True
    for digit in range(1, 10, 1):
        if possible(digit, row, col):
            board[row, col] = digit
            if solve():
                return True
    board[row, col] = 0

def solver():
    if solve(): return
    print('No solution found.')


if __name__ == '__main__':
    s = ['704000910',
         '000000000',
         '000000254',
         '008026040',
         '050003090',
         '900800700',
         '001005000',
         '800700002',
         '000210008']
    board = []
    for row in range(9):
        board.extend([int(x) for x in list(s[row])])
    board = np.array(board).reshape((9, 9))
    print_board()
    solver()