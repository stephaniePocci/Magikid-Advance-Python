"""
Things to talk about:
1. messagebox
2. photoimage
3. open thing
4. show info
5. choose color
"""

from tkinter import *

window = Tk()

# number 1
m1= Message(window, text="This is a message.", width=100)
m1.pack()

# number 2
image_path = "week13/shiba.png"  # Replace with the path to your image file
image = PhotoImage(file=image_path)

# Create a label to display the image
image_label = Label(window, image=image)
image_label.pack(pady=20)

# Add some text below the image
text_label = Label(window, text="This is a PhotoImage example.")
text_label.pack(pady=10)
# number 3
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

Button(window, text="Button", command=ask_options).pack()

# number 4
def click_me():
    # Displays a piece of information
    showinfo(title="Messagebox", message="showinfo()\nDisplays a piece of information")
    # Displays an error message
    showerror(title="Messagebox", message="showerror()\nDisplays an error message")
    # Displays a warning message
    showwarning(title="Messagebox", message="showwarning()\nDisplays a warning message")
    # Displays a question
    askquestion(title="Messagebox", message="askquestion()\nDisplays a question")
    # Displays a yes/no question. Returns True if Yes is selected
    askyesno(title="Messagebox", message="askyesno()\nDisplays a yes/no question. Returns True if Yes is selected")
    # Displays a yes/no/cancel question. 
    # Returns True if Yes is selected, and None if Cancel is selected
    askyesnocancel(title="Messagebox", message="askyesnocancel()\nDisplays a yes/no/cancel question. Returns True for Yes, None for Cancel")
    # Asks if the operation should continue. Returns True if OK is selected
    askokcancel(title="Messagebox", message="askokcancel()\nAsks if the operation should continue. Returns True for OK")
    # Asks if the user wants to retry an operation. Returns True if Retry is selected
    askretrycancel(title="Messagebox", message="askretrycancel()\nAsks if the user wants to retry an operation. Returns True for Retry")
    # Tip: You can add print() before each function to display the results of each call

# Button to trigger the click_me function
Button(text="Test Button", command=click_me).pack()

# number 5
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

window.mainloop()