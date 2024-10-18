from tkinter import *

window = Tk()

window.title("Entry Demo")

window.geometry('+1000+150')

lbl = Label(window, text="E-mail: ")
lbl.pack(side=LEFT)

en = Entry(window, bd=2)  
en.pack(side=RIGHT)

window.mainloop()
