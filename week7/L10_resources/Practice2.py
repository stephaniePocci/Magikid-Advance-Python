from tkinter import *

window = Tk()

window.title("Checkbutton Demo 2")

window.geometry('400x300')

lbl = Label(window, text="Empty",
            font=('Arial', 16),
            bg='yellow', fg='blue',
            width=24, height=2)
lbl.pack()


# Define trigger function function
def print_selection():
    if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0): 
        lbl.config(text="I do not love these")
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):  
        lbl.config(text="I love only Python")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 0):  
        lbl.config(text="I love only JavaScript")
    elif (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 1):  
        lbl.config(text="I love only C++")
    elif (var1.get() == 1) & (var2.get() == 1) & (var3.get() == 0):  
        lbl.config(text="I love Python and JavaScript")
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 1):  
        lbl.config(text="I love Python and C++")
    elif (var1.get() == 0) & (var2.get() == 1) & (var3.get() == 1):  
        lbl.config(text="I love JavaScript and C++")
    else:
        lbl.config(text='I love these all')  


# Define var1, var2 and var3 integer variables to store the return value of the selection behavior
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

# Set three options
cb1 = Checkbutton(window, text='Python',
                  variable=var1,
                  onvalue=1, offvalue=0,
                  command=print_selection)
cb1.pack()

cb2 = Checkbutton(window, text="JavaScript",
                  variable=var2,
                  onvalue=1, offvalue=0,
                  command=print_selection)
cb2.pack()

cb3 = Checkbutton(window, text="C++",
                  variable=var3,
                  onvalue=1, offvalue=0,
                  command=print_selection)
cb3.pack()

window.mainloop()
