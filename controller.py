from tkinter import Tk, Label, Button, mainloop, messagebox
from model import Model

class Controller():
    def __init__(self):
        self._model = Model()
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