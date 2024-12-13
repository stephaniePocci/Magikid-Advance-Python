from tkinter import *

window = Tk()

window.title("week 9")

window.geometry("1000x1000+2000+500")

def printValue(scale_one):
    print(scale_one)

scale1 = Scale(window, 
               from_=0, to=10, 
               length=800, 
               orient=HORIZONTAL, 
               showvalue=1, 
               tickinterval=1,
               resolution=2,
               activebackground='green',
               command=printValue
            )
scale1.pack()

cv = Canvas(window, width=200, height=200)
cv.pack()

# arrowshape = (length, width, wing width)
cv.create_line(0, 0, 200, 200, fill="red", width=10, arrow=LAST, arrowshape=(10, 10, 10))

cv.create_rectangle(50, 50, 100, 100, fill="green")

cv.create_text(30, 30, text="Silly Canvas", font=('Arial', 20))

x1= 0
y1 =0
x2 = 25
y2 = 25

rect = cv.create_rectangle(x1, y1, x2, y2, fill="blue")

cv.coords(rect, 50, 50, 100, 100)

window.mainloop()