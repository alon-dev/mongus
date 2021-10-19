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
        i = 0
        j = 0
        while True:
            i = randint(0, 2)
            j = randint(0, 2)
            if self.state[i, j] == "":
                self.state[i, j] = "O"
                break
        x = self.check_win()
        print(x)
        return i, j, x

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
        moves = Model.nextBoards(game_state, 0)
        best_move = moves[0]
        best_score = float('-inf')
        for move in moves:
            score = Model.min_play(move)
            if score > best_score:
                best_move = move
                best_score = score
        return best_move

    @ staticmethod
    def min_play(game_state, depth):
        if Model.is_win(game_state, 0):
            return 1
        elif Model.is_win(game_state, 1):
            return -1
        elif Model.is_tie(game_state):
            return 0
        moves = Model.nextBoards(game_state, 1)
        best_score = float()
        best_move=moves[0]
        for move in moves:
        score=Board.max_play(move)
        if score & lt; best_score:
        best_score=score
        return best_score
    
    @ staticmethod
    def max_play(game_state):
        # כמו בפעולה הקודמת
        moves = Board.nextBoards()
        best_score = float()
        best_move=moves[0]
        for move in moves:
        score=Board.min_play(move)
        if score & gt; best_score:
        best_score=score
        return best_score
