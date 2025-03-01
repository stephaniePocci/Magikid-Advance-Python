import tkinter as tk

# Initialize the main window
window = tk.Tk()
canvas_width = 700
canvas_height = 800

# Create the canvas
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="#006400")
canvas.pack()

# Create the ball
ball = canvas.create_oval(0, 0, 40, 40, fill="red")
canvas.move(ball, 330, 380)  # Initial position of the ball

# Ball movement variables
ball_x = 0
ball_y = -5

# Function to update the ball's position
def draw():
    global ball_x, ball_y

    # Move the ball
    canvas.move(ball, ball_x, ball_y)

    # Get the ball's current position
    position = canvas.coords(ball)

    # Reverse direction if the ball hits the top or bottom
    if position[1] <= 0:  # Top of the canvas
        ball_y = 5
    elif position[3] >= canvas_height:  # Bottom of the canvas
        ball_y = -5

    # Schedule the draw function to run again after 10 milliseconds
    window.after(10, draw)

# Start the animation
draw()

# Run the Tkinter main loop
window.mainloop()