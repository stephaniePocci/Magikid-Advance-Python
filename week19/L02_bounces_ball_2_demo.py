import tkinter as tk
import time

'''Step1:Setup window (setup game canvas)'''

window = tk.Tk()

canvas_width = 700
canvas_height = 800

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="#006400")
canvas.pack()

window.update()  # refresh page

'''Step2: Create a small ball on the canvas'''

# Draw a (colored) ball on canvas
ball1 = canvas.create_oval((0, 0), (40, 40), fill="red")
ball2 = canvas.create_oval((0, 0), (40, 40), fill="yellow")

# Put the ball into the canvas and set the initial position of the ball
canvas.move(ball1, 330, 380)
canvas.move(ball2, 330, 380)

# Set two variables as the initial movement mode of the ball
ball1_x = 0  
ball1_y = -5 

ball2_x = 0 
ball2_y = 5  


# Define the direction and speed of the ball
def draw():
    global ball1_x
    global ball1_y
    canvas.move(ball1, ball1_x, ball1_y)
    pos1 = canvas.coords(ball1)
    # Assign the coordinates of the ball (the ancestor of 4 numbers) to the variable pos1
    if pos1[1] <= 0:
        ball1_y = 5
    if pos1[3] >= canvas_height:
        ball1_y = -5

    global ball2_x
    global ball2_y
    canvas.move(ball2, ball2_x, ball2_y)
    pos2 = canvas.coords(ball2) 
    if pos2[1] <= 0:
        ball2_y = 5
    if pos2[3] >= canvas_height:
        ball2_y = -5


'''Step3:Create a main loop program and let the program run'''

while True:  
    draw()
    window.update()  
    time.sleep(0.01)

tk.mainloop()
