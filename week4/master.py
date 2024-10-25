# Things to teach
# 1. StringVar
# textvariable


# 2. trace
# 'w' : when the variable is written to (modified)
# 'r' : when the variable is read from
# 'u' : when the variable is deleted (unset)


# 3. Entry
# .get()
# .insert(): end insert


# 4. Text()

# 5. *args
# a. *args lets your function accept any number of inputs
# b. Inside the function, *args becomes a list of all the inputs
# c. You can use it when you don't know in advance how many inputs you'll get


# 6. Timer
# while loop sleep







from tkinter import *

# Step1: Create a main window named 'window'
window = Tk()

# Step2: Set window title named 'My Window'
window.title('Entry and Text')

# Step3: Set window size and position
window.geometry('400x300+1000+150')

# Step4: Create a 'Entry' widgets
entry = Entry(window, show=None, font=('Arial', 16))  # Show in plaintext
entry.pack()


# Step5: Define the functions insert_point and insert_end when two buttons trigger events
def insert_point():
    var_point = entry.get()
    text.insert('insert', var_point)


def insert_end():
    var_end = entry.get()  
    text.insert('end', var_end)  


# Step6: Create two buttons to trigger both cases
btn1 = Button(window, text='Insert Point', font=('Arial', 16), width=10,
              height=2, command=insert_point)
btn1.pack()

btn2 = Button(window, text='Insert End',
              font=('Arial', 16), 
              width=10, height=2,
              command=insert_end)
btn2.pack()

# Step7: Create 'Text' widgets
text = Text(window, font=('Arial', 16), height=3)
text.pack()

# Step8: Set the main window loop
window.mainloop()
