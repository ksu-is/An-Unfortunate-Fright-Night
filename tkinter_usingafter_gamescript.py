import random
import time
from tkinter import *


root = Tk()

#title of game
root.title("An Unfortunate Fright Night")
w = Label(root, text="An Unfortunate Fright Night.  A horror adventure text-based game!")
w.pack()

frame = Frame(root, width=600, height=600)
frame.pack()

#text box choose your option based on mutiple choice answers
L1 = Label(root, text="Choose your option: ")
L1.pack(side=LEFT)
E1 = Entry(root, bd =5)
E1.pack(side=LEFT)

#intro text
tiles_intro = ['It was a dark and spooky night.', 'You come across a haunted, abandoned house on your way to a Halloween party.', 'You are curious to see what is inside.', 'A. Go inside', 'B. Go to the party?']
tiles_intro.reverse()


def add_intro():
    if len(tiles_intro) > 0:
        intro_frame = Label(frame, text=tiles_intro.pop())
        intro_frame.pack()
        root.after(500, add_intro)
        


root.after(0, add_intro)  # add_intro will run as soon as the mainloop starts.
root.mainloop()


