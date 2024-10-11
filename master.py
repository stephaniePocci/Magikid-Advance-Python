# Pack and Label Stuff
from tkinter import *

leo = Tk()

leo.title('Test')

leo.resizable(0, 0)

leo.geometry('400x300+1000+150')

lbl1 = Label(leo, text='Test 1')
lbl1.pack(anchor=CENTER)
lbl2 = Label(leo, text='Test 2')
lbl2.pack(side=LEFT)
lbl3 = Label(leo, text='Test 3')
lbl3.pack(side=BOTTOM)
lbl4 = Label(leo, text='Test 4')
lbl4.pack(side=RIGHT)

# Global

from tkinter import *

window = Tk()

window.title("Label and Button")

window.geometry('400x300')

lbl = Label(window, text="You click me!", font=('Arial', 20), fg='white', bg='blue', height=2, width=16)
lbl.pack()

i = 0  


def click_me():
    global i  
    i = i + 1
    print("You click me " + str(i) + " time!")


btn = Button(window, text='Click Me', height=2, width=12, command=click_me)
btn.pack()

window.mainloop()

# Strings

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