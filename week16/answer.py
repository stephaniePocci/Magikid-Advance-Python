from tkinter import *

window = Tk()

window.title("calculator")

number = Label(window, text="ENTER NUMBER",
      bg='blue', fg='white',
      font=('Arial', 16))
number.pack()

input = StringVar()

def Enter():
    # Step 1: Initialize numbers
    global input
    stringInput = input.get()
    firstNum = ""
    operation = ""
    secondNum = ""
    isSecondNum = False;
    sum = 0

    # Step 2: lexical
    # TODO: Left off with this but they probably didnt do it right
    # How this works
    # loop through each character in stringInput
    # if isSecondNum is true that means we've gone past the operator and can now update secondNum by adding the character at i to it
    # else if the current value of stringInput[i] is an operator just update the operation value to it, and also set isSecondNum to true because following that characters should be a part of the second number
    # else let's assume we're still adding values to the firstNum
    for i in range(len(stringInput)):
        if isSecondNum:
                secondNum += stringInput[i]
            #     TODO: definitely did not handle the other operators
        elif (stringInput[i] == "+") or (stringInput[i] == "-") or (stringInput[i] == "/") or (stringInput[i] == "*"):
                operation = stringInput[i]
                isSecondNum = True
        else:
                firstNum += stringInput[i]
    
    # Step 3: Perform Operation
    # TODO: briefly mentioned this but only for subtract so they'll prob need guidance for the other operators
    if (operation == "+"):
          sum = int(firstNum) + int(secondNum)
    elif (operation == "-"):
          sum = int(firstNum) - int(secondNum)
    elif (operation == "*"):
          sum = int(firstNum) * int(secondNum)
    elif (operation == "/"):
          sum = int(firstNum) / int(secondNum)

    # Step 4: update label text
    # finally manually update value on the number label which is the label on line 7
    number.config(text=str(sum))
    # Step 5: reset variables
    input.set("")
    stringInput = ""
    firstNum = ""
    operation = ""
    secondNum = ""
    isSecondNum = False;
    sum = 0



def insertValue(value):
      # TODO:  talk about how to handle this

      # access the input variable in the local state
      global input
      # first get the current input string...
      # ex: # "12312+" 
      # then get the current value which is the argument from the lambda function
      # after that combine the two strings into one and update the input variable
      input.set(input.get() + value)
      # finally manually update value on the number label which is the label on line 7
      number.config(text=input.get())

# Create a main frame
frame_master = Frame(window)
frame_master.pack()

# Numpad
frame_left = Frame(frame_master)
frame_left.pack(side=LEFT)

# NOTE: to add a widget to a window you need to use .pack() but if you want to make 
# dynamic layouts like a grid then you need to use .grid() which specifies which
# row and column the widget is added. 

# EX a tic tac toe board will have row=0 and column=0 be the top left square,
# row=1 and column=1 be the middle square, and row=2 and column=2 be the bottom right

# NOTE: lambda is used as a way to call insertValue with a parameter
# lambdas are fancy ways to create and use functions once without using def
# you dont need to go over this because lowkey this might be complicated
# an example of this is using it as a one-liner but a trade off of that is that you would
# have to either declare the function again if you want to use it somewhere else.
Button(
      frame_left,
      text="1", 
      bg='white',
      command=lambda: insertValue("1")
      ).grid(row=0, column=0)
Button(
      frame_left,
      text="2", 
      bg='white',
      command=lambda: insertValue("2")
      ).grid(row=0, column=1)
Button(
      frame_left,
      text="3", 
      bg='white',
      command=lambda: insertValue("3")
      ).grid(row=0, column=2)
Button(
      frame_left,
      text="4", 
      bg='white',
      command=lambda: insertValue("4")
      ).grid(row=1, column=0)
Button(
      frame_left,
      text="5", 
      bg='white',
      command=lambda: insertValue("5")
      ).grid(row=1, column=1)
Button(
      frame_left,
      text="6", 
      bg='white',
      command=lambda: insertValue("6")
      ).grid(row=1, column=2)
Button(
      frame_left,
      text="7", 
      bg='white',
      command=lambda: insertValue("7")
      ).grid(row=2, column=0)
Button(
      frame_left,
      text="8", 
      bg='white',
      command=lambda: insertValue("8")
      ).grid(row=2, column=1)
Button(
      frame_left,
      text="9", 
      bg='white',
      command=lambda: insertValue("9")
      ).grid(row=2, column=2)

# Operators
frame_right = Frame(frame_master, bg='black')
frame_right.pack(side=RIGHT)
Button(
      frame_right,
      text="+", 
      bg='white',
      command=lambda: insertValue("+")
      ).pack()
Button(
      frame_right,
      text="-", 
      bg='white',
      command=lambda: insertValue("-")
      ).pack()
Button(
      frame_right,
      text="/", 
      bg='white',
      command=lambda: insertValue("/")
      ).pack()
Button(
      frame_right,
      text="*", 
      bg='white',
      command=lambda: insertValue("*")
      ).pack()
Button(
      frame_right,
      text="Enter", 
      bg='white',
      command=Enter
      ).pack()

window.mainloop()