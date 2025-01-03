from tkinter import *

window = Tk()

m1 = Message(window, text="This is a message.", width=100)
m1.pack()

m2 = Message(window, text="This is a very long and long message.", width=100)
m2.pack()

window.mainloop()
    