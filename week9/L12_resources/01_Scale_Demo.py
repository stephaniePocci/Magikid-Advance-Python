from tkinter import *

window = Tk()

window.title("Scale Demo")

scale1 = Scale(window,
               from_=0, to=10)  # Set the maximum and minimum values.
# Note that it is not 'from', but'from_'
scale1.pack()

scale2 = Scale(window,
               from_=0, to=100,
               orient=HORIZONTAL)  # Set the horizontal direction.
#If this parameter is not written, the default is vertical.；
scale2.pack()


def print_values():
    print(scale1.get(), scale2.get())


btn = Button(window,
             text="Print Values", 
             command=print_values)
btn.pack()

window.mainloop()
