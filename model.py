import numpy as np

class Model:
    def __init__(self) -> None:
        self.state = np.array([
            ["","",""],
            ["","",""],
            ["","",""]
            ])
        self.winner = ""
    def check_win(self):
        for i in range(2):
            if (self.state[i][0] == self.state[i][1] == self.state[i][2] != "") or (self.state[0][i] == self.state[1][i] == self.state[2][i] != "") or (self.state[0][0] == self.state[1][1] == self.state[2][2] != ""):
                return 0
        
        if '' not in self.state[0] and '' not in self.state[1] and '' not in self.state[2]:
            return 1
        return 2
    def place(self, i, j, item: str):
        if self.state[i,j] == "":
            self.state[i,j] = item
            return 0
        else:
            return 1