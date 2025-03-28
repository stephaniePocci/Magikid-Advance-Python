from turtle import * 
from math import *

# Step 1: window setting
width = 950
height = 500
setup(width, height)

# step 2: 
def pen_goto(x, y):
    up() # lifts the pen from the "paper"
    goto(x,y)
    down() # places the pen down to draw

speed(0) #1 is very slow and 10 is very fast, 0 is the fastest

# step 3: drawing the stripes
color('#b22234')
start_y = height/2 
spacing = (height / 13) * 2
for stripes in range(7):
    pen_goto(- width / 2, start_y)
    begin_fill()
    for i in range(2):
        fd(width)
        right(90)
        fd(height/13)
        right(90)
    end_fill()
    start_y -= spacing

# step 4 is the drawing
pen_goto(- width / 2, height/2)
color("#3c3b6e")
begin_fill()
for i in range(2):
    fd(width/5 *2)
    rt(90)
    fd(height/13 * 7)
    rt(90)
end_fill()

# step 5: drawing reference line
E = height / 13 * 7 / 10
G = width / 5 * 2 / 12

def ref_line():
    row_y = height / 2
    for row_line in range(9):
        row_y -= E
        pen_goto(- width / 2, row_y)
        fd(width / 5 * 2)
    
    setheading(-90)

    col_x = - width / 2
    for col_line in range(11):
        col_x += G
        pen_goto(col_x, height / 2)
        fd(height / 13 * 7)

# step 6: making the stars
L = height / 13
start_diameter = L / 5 * 4
star_radius = start_diameter / 2
start_side_len = sin(radians(36)) / cos(radians(36)) * star_radius

def star():
    for double_side in range(5): # points on the star
        fd(start_side_len) # sin(36 degrees) / cos (36 degrees) * start_radius
        lt(72)
        fd(start_side_len)
        rt(144)

def all_star():
    X = - width / 2 + G
    Y = height / 2 - E + star_radius
    for star_row in range(5):
        for row in range(6):
            pen_goto(X, Y)
            setheading(-72)
            begin_fill()
            star()
            end_fill()
            X += 2 * G
        X = - width / 2 + G
        Y -= 2 * E

    X = - width /2 + 2 * G
    Y = height / 2 - 2 * E + star_radius

    for star_row in range(4):
        for row in range(5):
            pen_goto(X,Y)
            setheading(-72)
            begin_fill()
            star()
            end_fill()
            X += 2 * G
        X = - width /2 + 2 * G
        Y -= 2 * E

ht()
color("white")
ref_line()
tracer(5, 0)
all_star()
done()