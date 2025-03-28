# The Flag of US

from turtle import *

"""
Hoist (height) of the flag: A = 1.0
Fly (width) of the flag: B = 1.9
"""

# Step 1: window setting
width = 950  # 1.9 * 600
height = 500  # 1.0 * 600
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

speed(0)

# Step 3: Drawing strips
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


# Step 4: Drawing federal
pen_goto(- width / 2, height/2)
color("#3c3b6e")
begin_fill()
for i in range(2):
    fd(width / 5 * 2)
    rt(90)
    fd(height / 13 * 7)
    rt(90)
end_fill()


done()
