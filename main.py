import numpy as np

count = 0
wins = []
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

def is_win(board):
    win = False
    item = ' '
    valid_win = True
    for i in [0,3,6]:
        if (board[i] == board[i+1] == board[i+2]) and board[i] != ' ':
            if win == False:
                win = True
                item = board[i]
            else:
                if item != board[i]:
                    valid_win = False
    for i in [0, 1, 2]:
        if (board[i] == board[i + 3] == board[i + 6]) and board[i] != ' ':
            if win == False:
                win = True
                item = board[i]
            else:
                if item != board[i]:
                    valid_win = False
    if (board[0] == board[4] == board[8]) and board[0] != ' ' or \
       (board[2] == board[4] == board[6]) and board[2] != ' ':
        if win == False:
                win = True
                item = board[0]
        else:
            if item != board[0]:
                valid_win = False
    return win, valid_win, item

def valid(board):
        x_count = 0
        o_count = 0
        for i in range(9):
            if board[i] == 'X':
                x_count = x_count + 1
            elif board[i] == '0':
                o_count = o_count + 1
        win = is_win(board)
        if win[0] == False:
            return (x_count - o_count <= 1) and (x_count - o_count >= 0)
        if win == (True, True, "X"):
            return x_count - o_count == 1
        elif win == (True, True, "O"):
            return x_count - o_count == 0
        if win[1] == False:
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
    if valid(board) and is_win(board)[0] and location == 9: # trimming
        if not any((board == ).all() for x in y):
            count = count + 1
            print(board)
            wins.append(board)
        return
    elif valid(board) and full(board) and location == 9:  # filtering
        if not (np.array(board) == np.array(wins)).all(1).any():
            count = count + 1
            print(board)
            wins.append(board)
        return
    if (location == 9):
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
print(count)
#recurse_board_time(board, True)