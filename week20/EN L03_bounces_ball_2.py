import tkinter as tk
import time
import random

'''Step1: Set up the window (set up the game canvas)'''

window = tk.Tk()

canvas_width = 700
canvas_height = 800

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="#006400")
canvas.pack()

window.update() 

'''Step2: Create a small ball on the canvas'''

# Draw a (colored) ball on canvas
ball1 = canvas.create_oval((0, 0), (40, 40), fill="red")
ball2 = canvas.create_oval((0, 0), (40, 40), fill="yellow")

# Put the ball into the canvas and set the initial position of the ball
canvas.move(ball1, 330, 200)
canvas.move(ball2, 330, 560)

'''Change the initial direction of the ball'''
start_x = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

# Set two variables as the initial movement direction of the ball
ball1_x = random.choice(start_x)
ball1_y = random.choice(start_x)
print("(" + str(ball1_x) + ", " + str(ball1_y) + ")")

ball2_x = random.choice(start_x)
ball2_y = random.choice(start_x)
print("(" + str(ball2_x) + ", " + str(ball2_y) + ")")


# Define the direction and speed of the ball
def draw():
    global ball1_x
    global ball1_y
    canvas.move(ball1, ball1_x, ball1_y)
    pos1 = canvas.coords(ball1)  
    '''top and bottom'''
    if pos1[1] <= 0:  # pos1 = [x1, y1, x2, y2] [330.0, 215.0, 370.0, 255.0]
        ball1_y = -ball1_y
    if pos1[3] >= canvas_height:
        ball1_y = -ball1_y
    '''left and right'''
    if pos1[0] <= 0:  # pos1 = [x1, y1, x2, y2] [330.0, 215.0, 370.0, 255.0]
        ball1_x = -ball1_x
    if pos1[2] >= canvas_width:
        ball1_x = -ball1_x

    global ball2_x
    global ball2_y
    canvas.move(ball2, ball2_x, ball2_y)
    pos2 = canvas.coords(ball2)  
    '''top and bottom'''
    if pos2[1] <= 0:  # pos1 = [x1, y1, x2, y2] [330.0, 215.0, 370.0, 255.0]
        ball2_y = -ball2_y
    if pos2[3] >= canvas_height:
        ball2_y = -ball2_y
    '''left and right'''
    if pos2[0] <= 0:  # pos1 = [x1, y1, x2, y2] [330.0, 215.0, 370.0, 255.0]
        ball2_x = -ball2_x
    if pos2[2] >= canvas_width:
        ball2_x = -ball2_x


'''Step3: Create the main loop program and let the program run'''

while True: 
    draw()
    window.update()  
    time.sleep(0.01)

tk.mainloop()
