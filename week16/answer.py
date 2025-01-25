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
    for i in range(len(stringInput)):
        if isSecondNum:
                secondNum += stringInput[i]
        elif (stringInput[i] == "+") or (stringInput[i] == "-") or (stringInput[i] == "/") or (stringInput[i] == "*"):
                operation = stringInput[i]
                isSecondNum = True
        else:
                firstNum += stringInput[i]
    
    # Step 3: Perform Operation
    if (operation == "+"):
          sum = int(firstNum) + int(secondNum)
    elif (operation == "-"):
          sum = int(firstNum) - int(secondNum)
    elif (operation == "*"):
          sum = int(firstNum) * int(secondNum)
    elif (operation == "/"):
          sum = int(firstNum) / int(secondNum)

    # Step 4: update label text
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
      global input
      input.set(input.get() + value)
      number.config(text=input.get())

# Create a main frame
frame_master = Frame(window)
frame_master.pack()

# Numpad
frame_left = Frame(frame_master)
frame_left.pack(side=LEFT)
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