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

#intro text, doesn't work

intro1 = Label(text="It was a dark and spooky night.")
intro1.grid(column=0, row=1)
intro2 = tk.Label(text="You come across a haunted, abandoned house on your way to your friend's Halloween party.")
intro2.grid(column=0, row=2)
intro3 = tk.Label(text="You are curious to see what is inside.")
intro3.grid(column=0, row=3)
intro4 = tk.Label(text='Go inside or Go to the party?')
intro4.grid(column=0, row=4)
intro5 = tk.Label(text='...')
intro5.grid(column=0, row=5)

#text box choose your option based on mutiple choice answers

L1 = Label(root, text="Choose your option: ")
L1.pack(side=LEFT)
E1 = Entry(root, bd =5)
E1.pack(side=LEFT)



#mutiple choice options appear in gui
tiles_letter = ['a', 'b', 'c', 'd', 'e']
tiles_letter.reverse()


def add_letter():
    if len(tiles_letter) > 0:
        tile_frame = Label(frame, text=tiles_letter.pop())
        tile_frame.pack()
        root.after(500, add_letter)



root.after(0, add_letter)  # add_letter will run as soon as the mainloop starts.
root.mainloop()
