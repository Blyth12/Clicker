import tkinter
from tkinter import ttk
from tkinter import *
import os


def raise_frame(frame):
    frame.tkraise()


root = Tk()

root.geometry('300x200')
root.title('I hate tillmann')

f1 = Frame(root)
f2 = Frame(root)
s = Frame(root)


root.resizable(width=False, height=False)

for frame in (f1, f2, s):
    frame.grid(row=20, column=20, sticky='news')


clicks = tkinter.IntVar()
inc = tkinter.IntVar()


def clicked(event=None):
   clicks.set(clicks.get() + inc)


def increase(event=None):
    inc.set(inc.get() + 2)


#img = PhotoImage(file='Assets\c.png')

#menu frame
b1 = tkinter.Button(f1,text='Go to game', fg="dark green", bg="white", command=lambda:raise_frame(f2)).grid(row=1, column=2, sticky=W)
b2 = tkinter.Button(f1, text='Quit', fg="red", bg="white", command=lambda:quit()).grid(row=1, column=3, sticky=W)
ml = tkinter.Label(f1, text='Menu', fg="dark green").grid(row=1, column=1, sticky=W)

#game frame
gl = tkinter.Label(f2, text='Game', fg="dark green").grid(row=1, column=1, sticky=W)
b3 = tkinter.Button(f2, text='Return to menu', fg="dark green", bg="white", command=lambda:raise_frame(f1)).grid(row=1, column=2, sticky=W)
b4 = tkinter.Button(f2, text='Go to the shop', fg="dark green", bg="white", command=lambda:raise_frame(s)).grid(row=1, column=3, sticky=W)
#gc = tkinter.Label(f2,image=img).grid(row=3, column=3, sticky=W)
bs = tkinter.Label(f2, text='').grid(row=5, column=3, sticky=W)
bs1 = tkinter.Label(f2, text='').grid(row=6, column=3, sticky=W)
ic = tkinter.Button(f2, text="Increase", command=clicked, fg="dark green", bg="white").grid(row=7, column=3, sticky=W)
ca = tkinter.Label(f2, textvariable=clicks, fg="dark green").grid(row=8, column=3, sticky=W)

#shop frame
st = tkinter.Label(s, text='The shop', fg="dark green").grid(row=1, column=1, sticky=W)
s1 = tkinter.Button(s, text='Return', fg="dark green", bg="white", command=lambda:raise_frame(f2)).grid(row=1, column=2, sticky=W)
bs3 = tkinter.Label(s, text='').grid(row=2, column=1, sticky=W)
bb1 = tkinter.Button(s, text="Test (+2 ppc)", command=increase, fg="dark green", bg="white").grid(row=3, column=1, sticky=W)
ds = tkinter.Label(s, textvariable=clicks, fg="dark green").grid(row=3, column=2, sticky=W)
mp = tkinter.Label(s, textvariable=inc, fg="dark green").grid(row=3, column=3, sticky=E)

raise_frame(f1)
root.mainloop()
