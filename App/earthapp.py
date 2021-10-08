import tkinter
from tkinter import ttk
from tkinter import *


def raise_frame(frame):
    frame.tkraise()


root = Tk()

root.geometry('500x500')

f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
    frame.grid(row=5, column=5, sticky='news')

#menu frame
b1 = tkinter.Button(f1,text='Go to frame 2', command=lambda:raise_frame(f2)).grid(row=1, column=5, sticky=W)
b2 = tkinter.Button(f1, text='Quit', command=lambda:quit()).grid(row=2, column=5, sticky=W)
Label(f1, text='Menu').grid(row=3, column=5, sticky=W)

#countries frame
Label(f2, text='Map').grid(row=2, column=5, sticky=W)
lbl = ttk.Label(f2, text = "Enter search query").grid(row=4, column=6, sticky=W)
b3 = tkinter.Button(f2, text='Go to frame 1', command=lambda:raise_frame(f1)).grid(row=4, column=5, sticky=W)
Label(f2, text='Search Countries Here!').grid(row=3, column=5, sticky=W)

raise_frame(f1)
root.mainloop()
