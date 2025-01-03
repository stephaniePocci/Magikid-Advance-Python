from tkinter import *
from tkinter.colorchooser import *

window = Tk()

window.title("Colorchooser Practice")


def choose_color():
    color = askcolor(color="#ffff00",
                      title="Color Chooser")
    print(color)


Button(text='Choose Color',
       fg="darkgreen",
       command=choose_color).pack(side=LEFT, padx=10)

Button(text='Quit',
       command=window.quit,
       fg="red").pack(side=LEFT, padx=10)

mainloop()
