"""
Challenge

1. create a canvas with just one square in it
2. create 3 scales
3. make the scales move the squares x, y, and size of the square


# EXTRA CHALLENGE
1. add a radio button to pick different shapes
2. add a button to add multiple shapes
3. add a clear button

"""

from tkinter import *

window = Tk()

window.title("week 9")

window.geometry("1000x1000+2000+500")

x1 = 0
y1 = 0
x2 = 25
y2 = 25
3
def moveShape(scale_one):
    global x1, x2, y1, y2
    
    x1_new = x1 + (int(scale_one) * 10)
    x2_new = x2 + (int(scale_one) * 10)
    y1_new = y1 + (int(scale_one) * 10)
    y2_new = y2 + (int(scale_one) * 10)
    cv.coords(rect, x1_new, y1_new, x2_new, y2_new)

scale1 = Scale(window, 
               from_=0, to=10, 
               length=800, 
               orient=HORIZONTAL, 
               showvalue=1, 
               tickinterval=2,
               resolution=2,
               activebackground='green',
               command=moveShape
            )
scale1.pack()

cv = Canvas(window, width=200, height=200)
cv.pack()

rect = cv.create_rectangle(x1, y1, x2, y2, fill="blue")

window.mainloop()