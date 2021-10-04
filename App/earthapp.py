import tkinter
from tkinter import *


def raise_frame(frame):
    frame.tkraise()


root = Tk()

root.geometry('500x500')

f1 = Frame(root)
f2 = Frame(root)

for frame in (f1, f2):
    frame.grid(row=5, column=5, sticky='news')

B1 = tkinter.Button(f1, text='Go to frame 2', command=lambda:raise_frame(f2)).pack()
B2 = tkinter.Button(f1, text='Quit', command=lambda:quit()).pack()
Label(f1, text='FRAME 1').pack()

Label(f2, text='FRAME 2').pack()
B3 = tkinter.Button(f2, text='Go to frame 1', command=lambda:raise_frame(f1)).pack()

raise_frame(f1)
root.mainloop()
