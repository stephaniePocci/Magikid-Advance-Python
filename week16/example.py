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

    # Step 2: lexical analysis
    """
        1. Loop through each character in stringInput
        2. Check if we are adding values to the secondNum
            -> if we are then add the current value to secondNum
        3. Check for operators + - / * 
            -> if we are then override operation to that value and set isSecondNum to True
        4. if the other two checks are false then just add the value to firstNum

    """
    for i in range(len(stringInput)):
        if isSecondNum:
            secondNum += stringInput[i]
        elif (stringInput[i] == "+" or stringInput[i] == "-" or stringInput[i] == "*" or stringInput[i] == "/"):
            operation = stringInput[i]
            isSecondNum = True
        else:
            firstNum += stringInput[i]
    # Step 3: Perform Operation
    """
        Using the variable operation we defined, either add, subtract, multiply, or divide firstNum and secondNum
    """
    if operation == "+":
        sum = int(firstNum) + int(secondNum)

    # Step 4: update label text
    """
        update the label, we called number on line 7, with the sum 
    """

    # Step 5: reset variables
    input.set("")
    stringInput = ""
    firstNum = ""
    operation = ""
    secondNum = ""
    isSecondNum = False;
    sum = 0

def insertValue(value):
    # Using the input StringVar that is previously defined, 
    # update it so that it takes the previous version of the string and adds the value to the back of it.
    """
        EXAMPLE:
        input = "1234+"
        value = "5"
        
        # after your code

        input = "1234+5"
    """
    # After that do not forget to update the label we called number on line 7

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