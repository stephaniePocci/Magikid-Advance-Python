import tkinter as tk
import time
import random

window = tk.Tk()

canvas_width = 700
canvas_height = 800

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="#006400")
canvas.pack()

window.update()

# draw a colored ball on the canvas
ball1 = canvas.create_oval((0, 0), (40, 40), fill="red")
ball2 = canvas.create_oval((0, 0), (40, 40), fill="yellow")

canvas.move(ball1, 330, 200)
canvas.move(ball2, 330, 560)

start_x = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

# set two variables as the initial movement direction
ball1_x = random.choice(start_x)
ball1_y = random.choice(start_x)

ball2_x = random.choice(start_x)
ball2_y = random.choice(start_x)

def draw():
    global ball1_x
    global ball1_y
    canvas.move(ball1, ball1_x, ball1_y)
    position1 = canvas.coords(ball1)

    #doesnt hit top and bottom
    if position1[1] <= 0:
        ball1_y = -ball1_y
    if position1[3] >= canvas_height:
        ball1_y = -ball1_y

    #doesnt hit let or right
    if position1[0] <= 0:
        ball1_x = -ball1_x
    if position1[2] >= canvas_width:
        ball1_x = -ball1_x

# create the main program loop
while True:
    draw()
    window.update()
    time.sleep(0.01)

tk.mainloop()