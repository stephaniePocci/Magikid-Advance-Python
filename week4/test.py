from tkinter import *

window = Tk()

m1 = Message(window, text="This is a very long message")
# m1.pack()

l1 = Label(window, text="This is a very long message")
# l1.pack()

image_path = 'week4/shiba.png'
image = PhotoImage(file=image_path)



image_label = Label(window, image=image, width=100, height=100)
image_label.pack()

from tkinter.filedialog import *

def ask_options():
    ask = asksaveasfilename()  # Choose a name for saving a file, returns the file name
    print(ask)
    ask = asksaveasfile()  # Choose a name for saving a file, creates the file and returns a file stream object
    print(ask)
    ask = askopenfilename()  # Choose a file to open, returns the file name
    print(ask)
    ask = askopenfile()  # Choose a file to open, returns an IO stream object
    print(ask)
    ask = askdirectory()  # Choose a directory, returns the directory name
    print(ask)
    ask = askopenfilenames()  # Choose multiple files to open, returns file names as a tuple
    print(ask)
    ask = askopenfiles()  # Choose multiple files to open, returns IO stream objects
    print(ask)

Button(window, text="ASK", command=ask_options, font=('Arial', 20)).pack()
window.mainloop()