from tkinter import *

window = Tk()

# lb1 = Label(window, text="Test", font=('Arial', 26), bg="green")
# lb1.pack(padx=20, pady=100)

# lb2 = Label(window, text="Test", font=('Arial', 26), bg="red")
# lb2.pack(ipadx=20, ipady=50)
window.geometry("300x300")


# rowspan = number, columnspan = number

gr1 = Label(window, text="Test", font=('Arial', 26), width=16, bg="green")
gr1.grid(row=0, column=0, columnspan=3)

gr2 = Label(window, text="Test", font=('Arial', 26), width=16, bg="blue")
gr2.grid(row=1, column=1, rowspan=3)

gr3 = Label(window, text="Test", font=('Arial', 26), width=16, bg="red")
gr3.grid(row=2, column=2, rowspan=2, columnspan=2, sticky=N)

window.mainloop()