from typing import List, Type
import numpy as np
from random import randint


class Model:
    def __init__(self) -> None:
        self.state = np.array([
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
            ])
        self.winner = ""

    def check_win(self):
        for i in range(3):
            if (self.state[i][0] == self.state[i][1] == self.state[i][2] != "") or (self.state[0][i] == self.state[1][i] == self.state[2][i] != "") or (self.state[0][0] == self.state[1][1] == self.state[2][2] != "") or (self.state[2][0] == self.state[1][1] == self.state[0][2] != ""):
                print("o")
                return 0
        if '' not in self.state[0] and '' not in self.state[1] and '' not in self.state[2]:
            return 1
        return 2

    def place(self, i, j, item: str):
        if self.state[i, j] == "":
            self.state[i, j] = item
            return 0
        else:
            return 1

    def next_board(self):
        self.state = Model.minimax(self.state)
        x = self.check_win()
        print(x)
        return self.state, x
    
    @staticmethod
    def is_tie(board):
        for i in range(3):
            for j in range(3):
                if board[i,j] == "":
                    return False
        return True
    
    @staticmethod
    def is_win(board,player):
        for i in range(3):
            if (player == board[i][0] == board[i][1] == board[i][2] != "") or (player == board[0][i] == board[1][i] == board[2][i] != "") or (player == board[0][0] == board[1][1] == board[2][2] != "") or (player == board[2][0] == board[1][1] == board[0][2] != ""):
                return True
        return False

    @staticmethod
    def nextBoards(board, player: int) -> list:
        boards = []
        str_player = "X" if player is 1 else "0"
        for i in range(3):
            for j in range(3):
                if board[i, j] == "":
                    b = board.copy()
                    b[i, j] = str_player
                    boards.append(b)
        return boards

    @staticmethod
    def minimax(game_state):
        moves = Model.nextBoards(game_state,0)
        best_move = moves[0]
        best_score = float("-inf")
        for move in moves:
            score = Model.min_play(move)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move
    @staticmethod
    def min_play(game_state):
        if Model.is_win(game_state,"0"):
            return -1
        elif Model.is_win(game_state,"X"):
            return 1
        elif Model.is_tie(game_state):
            return 0

        moves = Model.nextBoards(game_state,"X")
        best_score = float('inf')
        best_move = moves[0]
        for move in moves:
            score = Model.max_play(move)
            if score < best_score:
                best_score = score
        return  best_score
    
    @staticmethod
    def max_play(game_state):
        if Model.is_win(game_state,"0"):
            return -1
        elif Model.is_win(game_state,"X"):
            return 1
        elif Model.is_tie(game_state):
            return 0
        moves = Model.nextBoards(game_state,"0")
        best_score = float('-inf')
        best_move = moves[0]
        for move in moves:
            score = Model.min_play(move)
            if score > best_score:
                best_score = score
        return best_score

    
