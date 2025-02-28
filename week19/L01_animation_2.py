import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width=1000, height=500)
canvas.pack()

window.update()

redball = canvas.create_oval(450, 200, 550, 300, fill="red")

for i in range(90):
    canvas.move(redball, 5, 0)
    window.update()

while True:
    for i in range(180):
        canvas.move(redball, -5, 0)
        window.update()

    for i in range(180):
        canvas.move(redball, 5, 0)
        window.update()

tk.mainloop()
