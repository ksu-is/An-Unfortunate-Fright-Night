from tkinter import *

def change(a=0):
    color_label.config(bg = "blue" if a & 1 else "purple")
    color_label.after(2000,change, a ^ 1 )
if __name__ == '__main__':
    win = Tk() 
    win.geometry("500x300")
    win.title('Demonstrating after event')
    color_label = Label(win)
    color_label.pack(expand=YES, fill=BOTH)
    change()
 
win.mainloop()
