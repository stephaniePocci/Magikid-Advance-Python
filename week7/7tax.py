from tkinter import *

window = Tk()

window.title("Radio")

window.geometry('400x300+2000+150')

# group radio button
group1 = StringVar()
group2 = StringVar()

# "answer selected"

l = Label(window, text="answer selected", font=('Times New Roman', 20), bg="green", fg="white")
l.pack(anchor=W, fill=X)

def print_selection():
    l.config(text="Select: " + group1.get())

def print_selection2():
    l.config(text="Select: " + group2.get())


rb1 = Radiobutton(window, text="answer 1", command=print_selection, variable=group1, value="A", font=('Times New Roman', 20))
rb1.pack()

rb2 = Radiobutton(window, text="answer 2", command=print_selection, variable=group1, value="B", font=('Times New Roman', 20))
rb2.pack()

rb3 = Radiobutton(window, text="answer 3", command=print_selection2, variable=group2, value="C", font=('Times New Roman', 20))
rb3.pack()

rb4 = Radiobutton(window, text="answer 4", command=print_selection2, variable=group2, value="D", font=('Times New Roman', 20))
rb4.pack()



window.mainloop()