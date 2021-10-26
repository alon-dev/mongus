from tkinter import Tk, Label, Button, mainloop, messagebox
from model import Model

class Controller():
    def __init__(self):
        self._model = Model()
        self.pc = False
    def callback(self, i, j, item):
        x = self._model.place(i, j, item)
        if x == 1:
            return 4
        if self._model.check_win() == 0:
            if item == "X":
                return 0
            else:
                return 1
        elif self._model.check_win() == 1:
            return 2
        else:
            return 3
    def play(self):
        state, win = self._model.next_board()
        print(win)
        if win == 0:
            n = 1
        elif win == 1:
            n = 2
        else:
            n = 3
        return state, n