import tkinter as tk
import time  # Import the time module

window = tk.Tk()

canvas = tk.Canvas(window, width=1000, height=500)
canvas.pack()

window.update()

redball = canvas.create_oval(450, 200, 550, 300, fill="red")

# Move the ball to the right
for i in range(90):
    canvas.move(redball, 5, 0)
    window.update()
    time.sleep(0.02)  # Add a delay of 0.02 seconds (20 milliseconds)

# Move the ball back and forth indefinitely
while True:
    for i in range(180):
        canvas.move(redball, -5, 0)
        window.update()
        time.sleep(0.02)  # Add a delay of 0.02 seconds (20 milliseconds)

    for i in range(180):
        canvas.move(redball, 5, 0)
        window.update()
        time.sleep(0.02)  # Add a delay of 0.02 seconds (20 milliseconds)

tk.mainloop()