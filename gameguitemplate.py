import tkinter as tk
window = tk.Tk()

window.title("An Unfortunate Fright Night")

window.geometry("600x600")


# LABEL
title = tk.Label(text="An Unfortunate Fright Night.  A horror adventure text-based game")
title.grid(column=0, row=0)

intro1 = tk.Label(text="It was a dark and spook night.")
intro1.grid(column=0, row=1)
intro2 = tk.Label(text="You come across a haunted, abandoned house on your way to your friend's Halloween party.")
intro2.grid(column=0, row=2)
intro3 = tk.Label(text="You are curious to see what is inside.")
intro3.grid(column=0, row=3)
intro4 = tk.Label(text='Go inside or Go to the party?')
intro4.grid(column=0, row=4)
intro5 = tk.Label(text='...')
intro5.grid(column=0, row=5)



