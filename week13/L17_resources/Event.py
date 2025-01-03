from tkinter import *

window = Tk()


def hello():
    print("Single Click, Button-l")


def quit():
    print("Double Click, so let's stop")
    import sys
    sys.exit()


widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('&lt;Button-1&gt;', hello)
widget.bind('&lt;Double-1&gt;', quit)
widget.mainloop()
