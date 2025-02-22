import tkinter as tk
import time
window = tk.Tk()
canvas = tk.Canvas(window, width=1000, height=500)
canvas.pack()
window.update()

redball = canvas.create_oval(450, 200, 550, 300, fill="blue")

for i in range(90):
    canvas.move(redball, 5, 0)
    window.update()
    time.sleep(0.001) # adds a delay of 20 milliseconds

# move ball back and forth forever
while True:
    for i in range(180):
        canvas.move(redball, -5, 0)
        window.update()
        time.sleep(0.001) 
    for i in range(180):
        canvas.move(redball, 5, 0)
        window.update()
        time.sleep(0.02)



tk.mainloop()

