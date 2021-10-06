import numpy as np

count = 0
wins = set()
def all_boards():
    i = 0
    for x0 in [' ', 'X', '0']:
        for x1 in [' ', 'X', '0']:
            for x2 in [' ', 'X', '0']:
                for x3 in [' ', 'X', '0']:
                    for x4 in [' ', 'X', '0']:
                        for x5 in [' ', 'X', '0']:
                            for x6 in [' ', 'X', '0']:
                                for x7 in [' ', 'X', '0']:
                                    for x8 in [' ', 'X', '0']:
                                            board = [x0,x1,x2,x3,x4,x5,x6,x7,x8]
                                            print(i, ':', board)
                                            i = i + 1

def is_win(board, item):
    for i in [0,3,6]:
        if (board[i] == board[i+1] == board[i+2] == item):
            return True
    for i in [0, 1, 2]:
        if (board[i] == board[i + 3] == board[i + 6] == item):
            return True
    if (board[0] == board[4] == board[8]) and board[0] == item or \
       (board[2] == board[4] == board[6]) and board[2] == item:
        return True
    return False

def valid(board):
        x_count = 0
        o_count = 0
        for i in range(9):
            if board[i] == 'X':
                x_count = x_count + 1
            elif board[i] == '0':
                o_count = o_count + 1
        if is_win(board, 'X') == True and is_win(board, '0') == False:
            return x_count - o_count == 1
        elif is_win(board, '0') == True and is_win(board, 'X') == False:
            return x_count - o_count == 0
        elif is_win(board, 'X') == True and is_win(board, '0') == True:
            return False
        elif full(board):
            return x_count - o_count == 1
        else:
            return False

def full(board):
    x_count = 0
    o_count = 0
    for i in range(9):
        if board[i] == 'X':
            x_count = x_count + 1
        elif board[i] == '0':
            o_count = o_count + 1
    return x_count + o_count == 9

def recursive_board_3(board, location):
    global count
    global wins
    if valid(board) and location >= 9: # trimming
        count = count + 1
        print(board)
        wins.add(tuple(board))
        return
    if location >= 9:
        return
    for x in [' ','X', '0']:
        board[location] = x                 # start
        recursive_board_3(board, location+1)# check all branches
        board[location] = ' '               # go back to check the other starts

def printb(board):
    b = ' '
    for i in [0,3,6]:
        for j in range(3):
            b = b + board[i+j]+','
        b = b + '\n '
    #print(board)
    print (b)
    print('-------')


board = [' ' for i in range(9)]
print('final')
recursive_board_3(board, 0)
print(len(wins))
#recurse_board_time(board, True)