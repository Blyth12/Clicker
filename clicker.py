import tkinter
from tkinter import ttk
from tkinter import *
import os


def raise_frame(frame):
    frame.tkraise()


root = Tk()

root.geometry('500x500')

f1 = Frame(root)
f2 = Frame(root)
s = Frame(root)

for frame in (f1, f2, s):
    frame.grid(row=5, column=5, sticky='news')

#menu frame
b1 = tkinter.Button(f1,text='Go to frame 2', command=lambda:raise_frame(f2)).grid(row=1, column=5, sticky=W)
b2 = tkinter.Button(f1, text='Quit', command=lambda:quit()).grid(row=2, column=5, sticky=W)
Label(f1, text='Menu').grid(row=3, column=5, sticky=W)

#game frame
Label(f2, text='Game').grid(row=2, column=1, sticky=W)
b3 = tkinter.Button(f2, text='Go to frame 1', command=lambda:raise_frame(f1)).grid(row=1, column=1, sticky=W)
b4 = tkinter.Button(f2, text='Go to the shop', command=lambda :raise_frame(s)).grid(row=3, column=3, sticky=W)


#shop frame
s1 = tkinter.Button(s,text='Return', command=lambda:raise_frame(f2)).grid(row=1, column=5, sticky=W)
Label(f1, text='Menu').grid(row=3, column=5, sticky=W)


raise_frame(f1)
root.mainloop()
