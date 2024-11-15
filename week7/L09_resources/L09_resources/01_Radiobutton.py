from tkinter import *

window = Tk()

window.title("Radiobutton Demo")

window.geometry('400x300+1000+150')

lbl = Label(window,
            text="Your educational background:", 
            font=('Arial', 16))
lbl.pack(anchor=W)

var = StringVar()

rb1 = Radiobutton(window,
                  text="Undergraduate",
                  variable=var,  
                  value="A")  
rb1.pack(anchor=W)

rb2 = Radiobutton(window,
                  text="master",
                  variable=var,
                  value="B")
rb2.pack(anchor=W)

rb3 = Radiobutton(window,
                  text="PhD",
                  variable=var,
                  value="C")
rb3.pack(anchor=W)

window.mainloop()
