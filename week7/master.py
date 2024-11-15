"""
Things to mention RADIOBUTTON:
1. Radiobutton
2. variable: group radio buttons together 
3. value: The value attribute represents the value assigned to that particular radio button when it is selected.
4. config: The .config() method (or its alias .configure()) can be called on any widget, like Label, Button, Frame, etc., to change its options.
5. Fill

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
"""


from tkinter import *

window = Tk()

window.title("Radiobutton Demo")

window.geometry('400x300+1000+150')

lbl = Label(window,
            text="Your educational background:", 
            font=('Arial', 16))
lbl.pack(anchor=W)

var = StringVar()

# Creating radio buttons

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

lbl = Label(window,
            font=('Arial', 16), text="Empty",
            bg='green', fg='white', height=2)
lbl.pack(fill=X)


def print_selection():
    lbl.config(text="You have selected " + var.get())


var = StringVar()
rb1 = Radiobutton(window, text="Option A",  
                  variable=var, 
                  value="A", 
                  command=print_selection)  
rb1.pack()

rb2 = Radiobutton(window, text="Option B",
                  variable=var, value="B",
                  command=print_selection)
rb2.pack()

rb3 = Radiobutton(window, text="Option C",
                  variable=var, value="C",
                  command=print_selection)
rb3.pack()

window.mainloop()

