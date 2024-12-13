from tkinter import *

window = Tk()

window.title("Menu Practice")

window.geometry('400x300')

lbl = Label(window,
      text="Empty",
      bg="green", fg="white",
      width=20, height=2)
lbl.pack()


def button_new():
    lbl.config(text="You click " + "New")


def button_open():
    lbl.config(text="You click " + "Open Python_File")


def button_save():
    lbl.config(text="You click " + "Save")


def button_help():
    lbl.config(text="You click " + "Help")


def button_about():
    lbl.config(text="You click " + "About")



menu_all = Menu(window)


menu_file = Menu(menu_all,
                 tearoff=1)

menu_all.add_cascade(label="File",  
                     menu=menu_file)  
menu_file.add_command(label="New",  
                      command=button_new)


menu_open = Menu(menu_file,
                 tearoff=0)
menu_file.add_cascade(label="Open",  
                      menu=menu_open)  
menu_open.add_command(label="Python File", 
                      command=button_open)

menu_file.add_command(label="Save",  
                      command=button_save)
menu_file.add_separator()  
menu_file.add_command(label="Exit",
                      command=window.quit)  

menu_help = Menu(menu_all, tearoff=0)
menu_all.add_cascade(label='Help',  
                     menu=menu_help)  
menu_help.add_command(label='Help',
                      command=button_help)
menu_help.add_command(label='About',
                      command=button_about)

window.config(menu=menu_all)  
window.mainloop() 
