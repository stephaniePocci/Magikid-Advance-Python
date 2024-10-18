# 1.Tk() 
# .title("Label and Button") 
# .geometry('400x300')
# .resizable(0, 0)
# Label(leo, text='Test 1')
# .pack(anchor=CENTER)
# Button(window, text='Click Me', height=2, width=12, command=click_me)
# .mainloop() 

# String var code
from tkinter import *

window = Tk()
window.title("Label and Button")
window.geometry('400x300')

var = StringVar()

lbl = Label(window, textvariable=var, font=('Arial', 20), fg='white',
            bg='blue', height=2, width=20)
lbl.pack()

i = 0

def click_me():
    global i
    i = i + 1
    var.set("You click me " + str(i) + " time!")

btn = Button(window, text='Click Me', height=2, width=12, command=click_me)
btn.pack()

window.mainloop()
# Countdown
from time import sleep

def cooldown(x):
    while True:
        x = x - 1
        sleep(1)



# Challenge

# Create a cookie clicker game

# GAIN POINTS
# +1 to have a custom title
# +1 to have a label as a heading
# +1 to move the bottom to the bottom right
# +1 to move the score tally to the bottom left
# +1 change the button text when clicked
# +3 add your own twist
        

# MEGA CHALLENGE
# +3 figure out how to make a minion to do the clicking


# Text box
        
from tkinter import *

# Step1: Create a main window named 'window'
window = Tk()

# Step2: Set window title named 'My Window'
window.title('My Window')

# Step3: Set window size and position
window.geometry('400x300+1000+150')

# Step4: Create 'Entry' widgets
entry1 = Entry(window, show='*', font=('Arial', 16))  # Show in ciphertext
entry2 = Entry(window, show=None, font=('Arial', 16))  # Show in plaintext
entry3 = Entry(window, show=None, font=('Times', 18, 'bold italic'))
entry1.pack()
entry2.pack()
entry3.pack()

# add text to the side
lbl = Label(window, text="E-mail: ")
lbl.pack(side=LEFT)

en = Entry(window, bd=2)  
en.pack(side=RIGHT)

# Add text box
text = Text(window, font=('Arial', 16), height=3)
text.pack()

# Insert

def insert_point():
    var_point = entry.get()
    text.insert('insert', var_point) # adds it to the cursor point


def insert_end():
    var_end = entry.get()  
    text.insert('end', var_end)  # adds it to the end of the text


# Step6: Create two buttons to trigger both cases
btn1 = Button(window, text='Insert Point', font=('Arial', 16), width=10,
              height=2, command=insert_point)
btn1.pack()

btn2 = Button(window, text='Insert End',
              font=('Arial', 16), 
              width=10, height=2,
              command=insert_end)
btn2.pack()

# Step5: Set the main window loop
window.mainloop()