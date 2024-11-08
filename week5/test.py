from tkinter import *

window = Tk()

window.title('Entry and Text')

window.geometry('400x300+2000+150')

keyword = "Sigma"
count = 0
mult = 1
currentCount = StringVar()
# pythons tkinter way of a dynamic variable that updates

def counter():
    global count
    global mult
    count += mult
    currentCount.set(str(count))

def checker():
    global mult
    if keyword == entry.get():
        mult += 2
        print("YOU INCREMENT IT")
    else:
        print("Nah Incorrect")
    
Label(window, textvariable=currentCount, font=('Arial', 16)).pack()

Button(window, text="click me", command=counter, font=('Arial', 16)).pack()

entry = Entry(window, show=None, font=('Arial', 16))  # Show in plaintext
entry.pack()

btn1 = Button(window, text='enter', font=('Arial', 16), width=10,
              height=2, command=checker)
btn1.pack()

window.mainloop()