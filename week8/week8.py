from tkinter import *

window = Tk()

window.title("Checkbutton Demo")

window.geometry("800x800+2000+500")

lbl = Label(window, text="Question",
            font=('Arial', 16),
            bg='yellow', fg='blue',
            width=24, height=2)
lbl.pack(fill=X)
# lb1.config(text="I do not love these")

var1 = IntVar()
var2 = IntVar()
var3= IntVar()

def printValue():
    if (var1.get() == 0) & (var2.get() == 0) & (var3.get() == 0):
        lbl.config(text="None Selected")
    elif (var1.get() == 1) & (var2.get() == 0) & (var3.get() == 0):
        lbl.config(text="Answer A Selected")
    elif (var2.get() == 1):
        lbl.config(text="Answer B Selected")
    elif (var3.get() == 1):
        lbl.config(text="Answer C Selected")

cb1 = Checkbutton(window, text="Answer A", variable=var1, onvalue=1, offvalue=0, command=printValue, font=('Arial', 16))
cb1.pack()
cb2 = Checkbutton(window, text="Answer B", variable=var2, onvalue=1, offvalue=0, command=printValue, font=('Arial', 16))
cb2.pack()
cb3 = Checkbutton(window, text="Answer C", variable=var3, onvalue=1, offvalue=0, command=printValue, font=('Arial', 16))
cb3.pack()

switch = False

def hideCB():
    global switch
    if(switch == False):
        cb3.pack(anchor=N)
        switch = True
    else:
        cb3.pack_forget()
        switch = False

Button(window, text="hide", command=hideCB).pack(anchor=S)

window.mainloop()