import tkinter as tk
from tkinter import *
import os


def raise_frame(frame):
    frame.tkraise()


root = Tk()
root.geometry('300x500')
root.title('Menu')

rootg = Toplevel()
rootg.geometry('300x500')
rootg.title('Game')

roots = Toplevel()
roots.geometry('300x500')
roots.title('Shop')

rootsu = Toplevel()
rootsu.geometry('300x500')
rootsu.title('Login')


f1 = tk.Frame(root)
f2 = tk.Frame(rootg)
s = tk.Frame(roots)
sl = tk.Frame(rootsu)

root.resizable(width=False, height=False)
rootg.resizable(width=False, height=False)
roots.resizable(width=False, height=False)

for frame in (f1, f2, s):
    frame.grid(row=3000, column=2000, sticky='news')


clicks = IntVar()
inc = IntVar()


def startinc(event=None):
    inc.set(inc.get() + 1)


def increase(event=None):
    inc.set(inc.get() + 1)


def clicked(event=None):
    clicks.set(clicks.get() + inc.get())


#img = PhotoImage(file='Assets\c.png')
#gc = tk.Label(f2,image=img).place(x=10, y=10)


#login frame
tk.Button(rootsu, width=15, height=5, text='Login', fg="dark green", bg="white", command=lambda:[rootg.deiconify(), root.withdraw()]).place(x=5, y=10)
tk.Button(rootsu, width=5, height=5, text='Quit', fg="red", bg="white", command=lambda:quit()).place(x=250, y=410)
tk.Label(rootsu, width=5, height=5, text='Menu', fg="dark green").place(x=270, y=10, anchor='c')

#menu frame
tk.Button(root, width=15, height=5, text='Signup/Login', fg="dark green", bg="white", command=lambda:[rootsu.deiconify(), root.withdraw()]).place(x=5, y=10)
tk.Button(root, width=5, height=5, text='Quit', fg="red", bg="white", command=lambda:quit()).place(x=250, y=410)
tk.Label(root, width=5, height=5, text='Menu', fg="dark green").place(x=270, y=10, anchor='c')

#game frame
tk.Label(rootg, width=5, height=5, text='Game', fg="dark green").place(x=270, y=10, anchor='c')
tk.Button(rootg, width=15, height=5,  text='Return to menu', fg="dark green", bg="white", command=lambda:[rootg.withdraw(), root.deiconify()]).place(x=175, y=410)
tk.Button(rootg, width=15, height=5, text='Go to the shop', fg="dark green", bg="white", command=lambda:[roots.deiconify(), root.withdraw()]).place(x=10, y=410)
tk.Button(rootg, width=10, height=5, text="Increase", command=clicked, fg="dark green", bg="white").place(x=150, y=300, anchor='c')
tk.Label(rootg, width=5, height=5, textvariable=clicks, fg="dark green").place(x=150, y=100, anchor='c')

#shop frame
tk.Label(roots, width=6, height=5, text='The shop', fg="dark green").place(x=270, y=10, anchor='c')
tk.Button(roots, width=15, height=5, text='Return', fg="dark green", bg="white", command=lambda:[rootg.deiconify(), roots.withdraw()]).place(x=175, y=410)
tk.Button(roots, width=15, height=5, text="Test (+2 ppc)", command=increase, fg="dark green", bg="white").place(x=1, y=50)
tk.Label(roots, width=5, height=5, textvariable=clicks, fg="dark green").place(x=175, y=150, anchor = 'c')
tk.Label(roots, width=5, height=5, textvariable=inc, fg="dark green").place(x=175, y=100, anchor='c')

roots.withdraw()
rootg.withdraw()
rootsu.withdraw()
startinc()
raise_frame(f1)
root.mainloop()
