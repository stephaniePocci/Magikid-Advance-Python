# The Flag of US

from turtle import *
from math import *

"""
Hoist (height) of the flag: A = 1.0
Fly (width) of the flag: B = 1.9
"""

# Step 1: window setting
height = 500  # 1.0 * 600
width = height * 1.9  # 1.9 * 600
setup(width, height)

"""
Hoist (height) of the canton ("union"):
C = 0.5385 (A × 7/13, spanning seven stripes)
Fly (width) of the canton:
D = 0.76 (B × 2/5, two-fifths of the flag width)
E = F = 0.0538 (C/10, One-tenth of the height of the canton)
G = H = 0.0633 (D/12, One twelfth of the width of the canton)
Diameter of star: K = 0.0616
(L × 4/5, four-fifths of the stripe width)
Width of stripe: L = 0.0769
(A/13, One thirteenth of the flag height)

colors:
#b22234 (red)
#3c3b6e (blue)
#ffffff (white)
"""


# Step 2:
def pen_goto(x, y):
    up()
    goto(x, y)
    down()


# Step 3: Drawing strips
speed(0)
color("#b22234")
start_y = height / 2  # named a var
spacing = (height / 13) * 2
for strips in range(7):
    pen_goto(- width / 2, start_y)
    begin_fill()
    for i in range(2):
        fd(width)
        right(90)
        fd(height / 13)
        right(90)
    end_fill()
    start_y -= spacing

# Step 4: Drawing federal area
pen_goto(- width / 2, height / 2)
color("#3c3b6e")
begin_fill()
for i in range(2):
    fd(width / 5 * 2)
    rt(90)
    fd(height / 13 * 7)
    rt(90)
end_fill()

# Step 5: Drawing reference line
E = height / 13 * 7 / 10  # E = F = C / 10
G = width / 5 * 2 / 12  # G = H = D / 12


def ref_line():
    row_y = height / 2
    for row_line in range(9):
        row_y -= E
        pen_goto(- width / 2, row_y)
        fd(width / 5 * 2)

    setheading(-90)

    col_x = - width / 2  # -570
    for col_line in range(11):
        col_x += G
        pen_goto(col_x, height / 2)
        fd(height / 13 * 7)


# Step 6: star
L = height / 13
star_diameter = L / 5 * 4  # ≈36.92
star_radius = star_diameter / 2
star_side_len = sin(radians(36)) / cos(radians(36)) * star_radius


def star():
    for double_side in range(5):
        fd(star_side_len)  # SIN(36°) / COS(36°) * star_radius
        lt(72)
        fd(star_side_len)
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

    X = - width / 2 + 2 * G
    Y = height / 2 - 2 * E + star_radius

    for star_row in range(4):
        for row in range(5):
            pen_goto(X, Y)
            setheading(-72)
            begin_fill()
            star()
            end_fill()
            X += 2 * G
        X = - width / 2 + 2 * G
        Y -= 2 * E


ht()
color("white")
ref_line()
tracer(5, 0)
all_star()

done()
