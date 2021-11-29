import tkinter as tk
from tkinter import *
import os


def raise_frame(frame):
    frame.tkraise()


root = tk.Tk()
root.geometry('300x500')
root.title('o')

rootg = tk.Tk()
rootg.geometry('300x500')
rootg.title('o')

roots = tk.Tk()
roots.geometry('300x500')
roots.title('o')


f1 = tk.Frame(root)
f2 = tk.Frame(rootg)
s = tk.Frame(roots)

root.resizable(width=False, height=False)

for frame in (f1, f2, s):
    frame.grid(row=3000, column=2000, sticky='news')


clicks = IntVar()
inc = IntVar()


def increase(event=None):
    inc.set(inc.get() + 1)


def clicked(event=None):
   clicks.set(clicks.get() + inc.get())

#img = PhotoImage(file='Assets\c.png')
#gc = tk.Label(f2,image=img).place(x=10, y=10)

#menu frame


b1 = tk.Button(root, width=15, height=5, text='Go to game', fg="dark green", bg="white", command=lambda:[rootg.deiconify(), root.withdraw()]).place(x=5, y=10)
b2 = tk.Button(root, width=5, height=5, text='Quit', fg="red", bg="white", command=lambda:quit()).place(x=250, y=410)
ml = tk.Label(root, width=5, height=5, text='Menu', fg="dark green").place(x=270, y=10, anchor='c')

#game frame
gl = tk.Label(rootg, width=5, height=5, text='Game', fg="dark green").place(x=270, y=10, anchor='c')
b3 = tk.Button(rootg, width=15, height=5,  text='Return to menu', fg="dark green", bg="white", command=lambda:[rootg.withdraw(), root.deiconify()]).place(x=175, y=410)
b4 = tk.Button(rootg, width=15, height=5, text='Go to the shop', fg="dark green", bg="white", command=lambda:[roots.deiconify(), root.withdraw()]).place(x=10, y=410)
ic = tk.Button(rootg, width=10, height=5, text="Increase", command=clicked, fg="dark green", bg="white").place(x=150, y=300, anchor='c')
ca = tk.Label(rootg, width=5, height=5, text='c', textvariable=clicks, fg="dark green").place(x=150, y=100, anchor='c')

#shop frame
st = tk.Label(roots, width=5, height=5, text='The shop', fg="dark green").place(x=270, y=10, anchor='c')
s1 = tk.Button(roots, width=5, height=5, text='Return', fg="dark green", bg="white", command=lambda:[rootg.deiconify(), roots.withdraw()]).place(x=10, y=1)
bb1 = tk.Button(roots, width=5, height=5, text="Test (+2 ppc)", command=increase, fg="dark green", bg="white").place(x=1, y=50)
ds = tk.Label(roots, width=5, height=5, textvariable=clicks, fg="dark green").place(x=10, y=10)
mp = tk.Label(roots, width=5, height=5, textvariable=inc, fg="dark green").place(x=50, y=1)

roots.withdraw()
rootg.withdraw()
raise_frame(f1)
root.mainloop()
