import random
import time
from tkinter import *


root = Tk()

w = Label(root, text="GAME")
w.pack()

frame = Frame(root, width=300, height=300)
frame.pack()

L1 = Label(root, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(root, bd =5)
E1.pack(side=LEFT)

tiles_letter = ['a', 'b', 'c', 'd', 'e']
tiles_letter.reverse()

def add_letter():
    tile_frame = Label(frame, text=tiles_letter.pop())
    tile_frame.pack()
    root.after(500, add_letter)

    if tiles_letter == []:
        return tiles_letter.pop()
    
root.after(0, add_letter)  # add_letter will run as soon as the mainloop starts.
root.mainloop()
