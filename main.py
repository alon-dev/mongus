import model
import numpy as np
c = model.Model()
states = []
def recursion1(state, turn):
    global states
    a = model.Model()
    a.state = state
    if a.check_win() != 2:
        found = False
        for item in states:
            d = np.array(item) == np.array(state)
            f = d.all()
            if f:
                found = True
        if not found:    
            states.append(list(a.state))
        return
    for i in range (3):
        for j in range(3):
            if state[i, j] == "":
                b = state.copy()
                b[i,j] = turn
                if turn == "X":
                    turn = "O"
                else:
                    turn = "X"
                recursion1(b, turn)
    return
recursion1(c.state, "X")
for state in states:
    state = np.array(state)
    print(state)