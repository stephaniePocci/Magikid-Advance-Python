# Flag of the United States

from turtle import *

# window settings
width = 1140  # 1.9 * 600 = 1140
height = 600  # 1.0 * 600 = 600
setup(width, height)


# Step 2:
def pen_goto(x, y):
    up()
    goto(x, y)
    down()


done()

'''
Hoist (height) of the flag: A = 1.0
Fly (width) of the flag: B = 1.9
'''

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
