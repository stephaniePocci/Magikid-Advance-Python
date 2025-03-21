import tkinter as tk
import random
import time

window = tk.Tk()
canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(window, width=canvas_width, height= canvas_height, bg="#008080")
canvas.pack()

ball_dm = 30
ball1 = canvas.create_oval((0,0), (ball_dm, ball_dm), fill="red")
canvas.move(ball1, (canvas_width - ball_dm) /2, (canvas_height - ball_dm) / 2)

paddle_width = 100
paddle_height = 20
paddle = canvas.create_rectangle(0, 0, paddle_width, paddle_height, fill="yellow")
canvas.move(paddle, (canvas_width - paddle_width) / 2, (canvas_height / 2 + 150))

start_x = [-4, -3, -2, 2, 3, 4]
ball1_x = random.choice(start_x)
ball1_y = -5

# tracking the key presses
keys_pressed = {"Left": False, "Right": False}

def move():
    global ball1_x, ball1_y

    #move ball
    canvas.move(ball1, ball1_x, ball1_y)
    pos1 = canvas.coords(ball1)
    pos2 = canvas.coords(paddle)

    # ball collision with top
    if pos1[1] <= 0:
        ball1_y = -ball1_y

    # ball collision with paddle
    if pos1[2] >= pos2[0] and pos1[0] <= pos2[2]:
        if pos2[1] <= pos1[3] <= pos2[3]:
            ball1_y = -ball1_y
    
    # ball goes out of bounds (bottom)
    if pos1[3] >= canvas_height:
        ball1_x = 0
        ball1_y = 0

    # ball collision with left and right walls
    if pos1[0] <= 0 or pos1[2] >= canvas_width:
        ball1_x = -ball1_x

def update_paddle():
    # move the paddle continuously if left or right is held down
    if keys_pressed["Left"]:
        canvas.move(paddle, -5, 0) # move left
    if keys_pressed["Right"]:
        canvas.move(paddle, 5, 0) # move right
    window.after(10, update_paddle) # run every 10 ms for smooth movement

def key_press(event):
    # set the key state to True when pressed 
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = True

def key_release(event):
    if event.keysym in keys_pressed:
        keys_pressed[event.keysym] = False

canvas.bind_all("<KeyPress>", key_press)
canvas.bind_all("<KeyRelease>", key_release)