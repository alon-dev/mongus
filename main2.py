from model import Model
import numpy as np
board = np.array([["X", "0", "X"],
                 ["", "0", "X"], 
                 ["X", "",""]])
for board in Model.nextBoards(board,1):
    print(board)
