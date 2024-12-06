from tkinter import *

window = Tk()

window.title("Scale Practice")

window.geometry('400x300')

lbl = Label(window,
            bg='green', fg='white',
            width=20, height=2,
            text="Empty")
lbl.pack()

# var = StringVar()


def print_selection(a):    
    lbl.config(text="You have selected " + a)
    # print(var.get())
    # print(v)


scale = Scale(window,
              label="try me",
              from_=0, to=10,
              orient=HORIZONTAL,
              length=300,
              showvalue=1,  # Whether to display the current value
              tickinterval=2,  # scale is 2
              resolution=1,  # The accuracy is 0.01
              command=print_selection)
scale.pack()

window.mainloop()
