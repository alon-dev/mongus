from controller import Controller
from tkinter import Menu, Tk, Label, Button, mainloop, messagebox
import sys
import os
from tkinter import Tk, Label, Button, mainloop, messagebox

class MyButton(Button):
    def __init__(self, master, i, j, view):
        super().__init__(master, text=" ", font=("Helvetica", 20), width=6, height=3, command = self.callback)
        self._i = i
        self._j = j
        self._view = view
    def callback(self):
        if self._view.turnx:
            item = "X"
        else:
            item = "O"
        x = self._view._controller.callback(self._i, self._j, item)
        if x == 4:
            messagebox.showerror("ERROR", "THIS TILE IS ALREADY TAKEN!")
            return
        if self._view.turnx:
            item = "X"
            self["text"] = "X"
            self._view.mainLabel["text"] = "It is now o's turn"
            self._view.turnx = False
        else:
            self["text"] = "O"
            self._view.mainLabel["text"] = "It is now x's turn"
            item = "O"
            self._view.turnx = True
        if x == 0:
            messagebox.showinfo("GAME OVER!", "X WINS!")
            self._view.mainLabel["text"] = "Game Over- X WINS!"
            self._view.mainLabel["fg"] = "red"
            self._view.b1["state"] = "disabled"
            self._view.b2["state"] = "disabled"
            self._view.b3["state"] = "disabled"
            self._view.b4["state"] = "disabled"
            self._view.b5["state"] = "disabled"
            self._view.b6["state"] = "disabled"
            self._view.b7["state"] = "disabled"
            self._view.b8["state"] = "disabled"
            self._view.b9["state"] = "disabled"
            return
        elif x == 1:
            messagebox.showinfo("GAME OVER!", "O WINS!")
            self._view.mainLabel["text"] = "Game Over- O WINS!"
            self._view.mainLabel["fg"] = "red"
            self._view.b1["state"] = "disabled"
            self._view.b2["state"] = "disabled"
            self._view.b3["state"] = "disabled"

            self._view.b4["state"] = "disabled"
            self._view.b5["state"] = "disabled"
            self._view.b6["state"] = "disabled"

            self._view.b7["state"] = "disabled"
            self._view.b8["state"] = "disabled"
            self._view.b9["state"] = "disabled"
            return
        elif x == 2:
            messagebox.showinfo("GAME OVER!", "TIE!")
            self._view.mainLabel["text"] = "Game Over- TIE!"
            self._view.mainLabel["fg"] = "red"
            self._view.b1["state"] = "disabled"
            self._view.b2["state"] = "disabled"
            self._view.b3["state"] = "disabled"

            self._view.b4["state"] = "disabled"
            self._view.b5["state"] = "disabled"
            self._view.b6["state"] = "disabled"

            self._view.b7["state"] = "disabled"
            self._view.b8["state"] = "disabled"
            self._view.b9["state"] = "disabled"
            return
class View:
    def __init__(self, master):
        self._controller = Controller()
        self.master = master
        self.turnx = True
        self.b1 = MyButton(master, 0, 0, self)
        self.b2 = MyButton(master, 0, 1, self)
        self.b3 = MyButton(master, 0, 2, self)

        self.b4 = MyButton(master, 1, 0, self)
        self.b5 = MyButton(master, 1, 1, self)
        self.b6 = MyButton(master, 1, 2, self)

        self.b7 = MyButton(master, 2, 0, self)
        self.b8 = MyButton(master, 2, 1, self)
        self.b9 = MyButton(master, 2, 2, self)

        self.mainLabel = Label(master, text= "It is now x's turn", font=("Helvetica", 20))
        self.resetButton = Button(master, text="Reset Game", font=("Helvetica", 20), command=self.restart)

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)

        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        self.mainLabel.grid(row=3, columnspan=3)
        self.resetButton.grid(row=4, columnspan=3)
        w = Menu(master)
        w.add_command(label="About", command= self.callback)
        self.master.config(menu=w)
        mainloop()
    def callback(self):
        messagebox.showinfo("About", "Alon Engel")
    def restart(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

root = Tk()
root.title("Tic Tac Toe")
my_gui = View(root)
root.mainloop()