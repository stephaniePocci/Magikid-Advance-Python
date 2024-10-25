from tkinter import *

# Step1: Create a main window named 'window'
window = Tk()

# Step2: Set window title named 'Typing Game'
window.title('Entry and Text')

# Step3: Set window size and position
window.geometry('400x300+1000+150')

# Step5: create a function that checks if a word is valid and have it print a correct

def check_word(*args):
    word = target.get()

    if word == "abc":
        print("yippie")
    else:
        print("nah")

# Step4: create a String var and have it trace to track changes whenever someone writes
target = StringVar()
target.trace('w', check_word)

# Step6: create an entry box and end the loop
entry = Entry(window, textvariable=target, show=None, font=('Arial', 16))  # Show in plaintext
entry.pack()

window.mainloop()



# Challenge1: create a list of target words and make the new target word update randomly once a person types it
# Challenge2: change the text so that it has color signals if the person is typing the write letter
# Challenge3: create a timer