import random
from tkinter import *
from random import randint
import time
import threading

root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

def placewindows():
    while True:
        win = Toplevel(root)
        win.geometry("300x70+" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(randint(0, root.winfo_screenheight() - 70)))
        win.overrideredirect(1)
        Label(win, text="Hacklendin", fg="red",font="Verdana 26 bold").place(relx=.15, rely=.2)
        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        time.sleep(.02)

threading.Thread(target=placewindows).start()

root.mainloop()