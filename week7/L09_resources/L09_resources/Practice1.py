from tkinter import *

window = Tk()

window.title("Radiobutton Demo 2")

lbl = Label(window,
            font=('Arial', 16), text="Empty",
            bg='green', fg='white',
            width=20, height=2)
lbl.pack()


def print_selection():
    lbl.config(text="You have selected " + var.get())


var = StringVar()
rb1 = Radiobutton(window, text="Option A",  
                  variable=var, 
                  value="A", 
                  command=print_selection)  
rb1.pack()

# rb2 = Radiobutton(window, text="Option B",
#                   variable=var, value="B",
#                   command=print_selection)
# rb2.pack()

# rb3 = Radiobutton(window, text="Option C",
#                   variable=var, value="C",
#                   command=print_selection)
# rb3.pack()

window.mainloop()
