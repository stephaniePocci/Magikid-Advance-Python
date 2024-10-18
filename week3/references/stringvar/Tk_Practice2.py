from tkinter import *

window = Tk()
window.title("Label and Button")
window.geometry('400x300')

# Set the content of the label tag as a character type, and use var to receive the
# outgoing content of the Click Me function to display on the label；
var = StringVar()

lbl = Label(window, textvariable=var, font=('Arial', 20), fg='white',
            bg='blue', height=2, width=20)
lbl.pack()

i = 0

def click_me():
    global i
    i = i + 1
    var.set("You click me " + str(i) + " time!")

btn = Button(window, text='Click Me', height=2, width=12, command=click_me)
btn.pack()

window.mainloop()
