from controller import Controller
from tkinter import Frame, Menu, Tk, Label, Button, Toplevel, mainloop, messagebox, ttk
import sys
import os
from tkinter import Tk, Label, Button, mainloop, messagebox

class MyButton(ttk.Button):
    def __init__(self, master, i, j, view):
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 20))
        super().__init__(master, text=" ", style="my.TButton", state="disabled", command = self.callback)
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
        if not self._view._controller.pc:
            if self._view.turnx:
                self["text"] = "X"
                self._view.mainLabel["text"] = "It is now o's turn"
                self._view.turnx = False
            else:
                self["text"] = "O"
                self._view.mainLabel["text"] = "It is now x's turn"
                self._view.turnx = True
        else:
            if self._view.turnx:
                self["text"] = "X"
            else:
                self["text"] = "O"
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
        if self._view._controller.pc:
            state, x = self._view._controller.play()
            for i in range(3):
                for j in range(3):
                    self._view.buttons[i][j]["text"] = state[i][j]
            if x == 1:
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
        a = ttk.Frame(master)
        left_a = ttk.Frame(a)
        left_a.grid(column=0)
        self.button = ttk.Button(left_a, text= "VS PC", command= self.callback1)
        self.button1 = ttk.Button(left_a, text= "VS Person", command= self.callback2)
        self.button.pack(expand=True, fill='both')
        self.button1.pack(expand=True, fill='both')

        b = Frame(master)
        self.turnx = True
        self.b1 = MyButton(b, 0, 0, self)
        self.b2 = MyButton(b, 0, 1, self)
        self.b3 = MyButton(b, 0, 2, self)

        self.b4 = MyButton(b, 1, 0, self)
        self.b5 = MyButton(b, 1, 1, self)
        self.b6 = MyButton(b, 1, 2, self)

        self.b7 = MyButton(b, 2, 0, self)
        self.b8 = MyButton(b, 2, 1, self)
        self.b9 = MyButton(b, 2, 2, self)
        right_a = ttk.Frame(a)
        right_a.grid(column=1)
        self.mainLabel = Label(right_a, text= "It is now x's turn", font=("Helvetica", 20))
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 20))
        self.resetButton = ttk.Button(right_a, text="Reset Game", style='my.TButton', command=self.restart)

        self.b1.grid(row=0, column=0, ipadx=20, ipady=40)
        self.b2.grid(row=0, column=1 ,ipadx=20, ipady=40)
        self.b3.grid(row=0, column=2, ipadx=20, ipady=40)
        
        self.b4.grid(row=1, column=0, ipadx=20, ipady=40)
        self.b5.grid(row=1, column=1, ipadx=20, ipady=40)
        self.b6.grid(row=1, column=2, ipadx=20, ipady=40)

        self.b7.grid(row=2, column=0, ipadx=20, ipady=40)
        self.b8.grid(row=2, column=1, ipadx=20, ipady=40)
        self.b9.grid(row=2, column=2, ipadx=20, ipady=40)
        b.pack()
        a.pack()
        self.buttons = []
        self.buttons.append([self.b1, self.b2, self.b3])
        self.buttons.append([self.b4, self.b5, self.b6])
        self.buttons.append([self.b7, self.b8, self.b9])
        self.mainLabel.pack()
        self.resetButton.pack()
        w = Menu(master)
        w.add_command(label="About", command= self.callback)
        self.master.config(menu=w)
        mainloop()
    def callback(self):
        messagebox.showinfo("About", "Alon Engel")
    def callback1(self):
        self._controller.pc = True
        self.button["state"] = "disabled"
        self.button1["state"] = "disabled"
        for buttons in self.buttons:
            for button in buttons:
                button["state"] = "normal"

    def callback2(self):
        self._controller.pc = False
        self.button["state"] = "disabled"
        self.button1["state"] = "disabled"
        for buttons in self.buttons:
            for button in buttons:
                button["state"] = "normal"
                
    def restart(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

root = Tk()
root.title("Tic Tac Toe")
my_gui = View(root)
root.mainloop()