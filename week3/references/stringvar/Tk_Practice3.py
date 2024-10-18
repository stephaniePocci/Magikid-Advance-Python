from tkinter import *

window = Tk()

window.title("Label and Button")

window.geometry('400x300+1000+150')

# Set the content of the label tag as a character type, and use var to
# receive the outgoing content of the hit_me function to display on the label；
var = StringVar()
var.set("Empty")

lbl = Label(window,
            textvariable=var,
            font=('Arial', 20),
            fg='white', bg='blue',
            height=2, width=16)
lbl.pack()

# Define a function function (write the content freely)
# for calling when the Button button is clicked；
on_click = False


def click_me():
    global on_click

    if not on_click:
        on_click = True
        var.set('You click me now!')
    else:
        on_click = False
        var.set('Empty')


btn = Button(window, text='Click Me', height=2, width=12, command=click_me)
btn.pack()

window.mainloop()
