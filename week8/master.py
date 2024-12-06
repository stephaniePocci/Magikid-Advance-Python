"""
Things to mention CHECKBUTTON
1. config
2. IntVar()
3. onvalue: value when selected
4. offvalue: value when deselected

OPTIONAL
bd: border width
padx: horizontal padding
pady: vertical padding
justify: Controls how multi-line text is aligned within the checkbutton label. (left, center, right)
relief: Defines the type of 3D border to display around the checkbutton. (flat, raised, sunken, groove, ridge)
wraplength: Sets the maximum width of the checkbutton’s text in pixels. If the text is longer, it wraps to the next line.
state: Controls whether the checkbutton is active or disabled. (normal, disabled, active)
selectcolor: change bg color when selected
selectimage: specifies and image to be displayed when the checkbutton is selected (PhotoImage)

deselect(): unchecks button
flash(): flash between active and normal states momentarily.
invoke(): Programmatically "clicks" the checkbutton. If the checkbutton has a command associated with it, the invoke() method will trigger that command. 
select(): checks a checkbutton
toggle(): changes the state between selected or deselected


EXTRA STUFF
window.after(miliseconds, function, *args)

"""

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





# TIMER

import tkinter as tk

def update_timer():
    global counter
    counter += 1
    label.config(text=f"Timer: {counter} seconds")
    root.after(1000, update_timer)  # Call this function again in 1 second

root = tk.Tk()
counter = 0
label = tk.Label(root, text="Timer: 0 seconds")
label.pack()

update_timer()  # Start the timer
root.mainloop()
