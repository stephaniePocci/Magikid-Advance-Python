from tkinter import *
window = Tk()

lb = Label(window, text="No Command Click", font=('Arial', 30))
lb.pack()

lb2 = Label(window, text="0", font=("Arial", 20))
lb2.pack()

counter = 0

def stop_watch():
    global counter
    counter += 1
    lb2.config(text=f"Timer: {counter}")
    window.after(1000, stop_watch)


def changeText():
    lb.config(text="Command Click")

menu_all = Menu(window)
menu_title = Menu(menu_all,
                 tearoff=0)
menu_all.add_cascade(label="File",  
                     menu=menu_title) 
menu_title.add_command(label="Start", command=stop_watch)
menu_title.add_command(label="Open", command=changeText)
menu_title.add_command(label="Save", command=changeText)

window.config(menu=menu_all)

window.mainloop()