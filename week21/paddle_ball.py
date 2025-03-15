import tkinter as tk
import time
import random

window = tk.Tk()

canvas_width = 700
canvas_height = 800

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="#006400")
canvas.pack()

window.update()

ball1_images = [
    tk.PhotoImage(file="images/bb1.png"),
    tk.PhotoImage(file="images/bb2.png"),
    tk.PhotoImage(file="images/bb3.png")
]

ball1 = canvas.create_image(canvas_width/2, canvas_height/2, image=ball1_images[0])

image_index = 0

def animate():
    global image_index
    image_index += 1
    canvas.itemconfig(ball1, image=ball1_images[image_index % 3])

def ball1_coords():
    ball1_xy = canvas.coords(ball1)
    x1 = ball1_xy[0] - 20
    y1 = ball1_xy[1] - 20
    x2 = ball1_xy[0] + 20
    y2 = ball1_xy[1] + 20
    return [x1, y1, x2, y2]

start_x = [-10, -6, -2, 2, 6, 10]
ball1_x = random.choice(start_x)
ball1_y = 10

def move():
    animate()
    global ball1_x
    global ball1_y
    canvas.move(ball1, ball1_x, ball1_y)
    pos1 = ball1_coords()
    # top or bottom
    if pos1[1] <= 0:
        ball1_y = -ball1_y
    if pos1[3] >= canvas_height:
        ball1_y = -ball1_y
    # left or right
    if pos1[0] <= 0:
        ball1_x = -ball1_x
    if pos1[2] >= canvas_width:
        ball1_x = -ball1_x

while True:
    move()
    window.update_idletasks()
    window.update()
    time.sleep(0.03)