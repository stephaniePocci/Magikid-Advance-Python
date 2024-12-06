from tkinter import *

window = Tk()

window.title("Canvas Practice")

canvas_width = 200
canvas_height = 100

colours = ("#4169E1", "yellow")
box = []

for ratio in (0.2, 0.35):  
    box.append((canvas_width * ratio,  
                canvas_height * ratio,  
                canvas_width * (1 - ratio),  
                canvas_height * (1 - ratio)))  


cv = Canvas(window,
            width=canvas_width,
            height=canvas_height)
cv.pack()

for i in range(2):
    cv.create_rectangle(box[i][0], box[i][1], box[i][2], box[i][3], fill=colours[i])

cv.create_line(0, 0,  
               box[0][0], box[0][1],  
               fill=colours[0],
               width=3)
cv.create_line(0, canvas_height,  
               box[0][0], box[0][3],  
               fill=colours[0],
               width=3)
cv.create_line(box[0][2], box[0][1],  
               canvas_width, 0,  
               fill=colours[0],
               width=3)
cv.create_line(box[0][2], box[0][3],  
               canvas_width, canvas_height,  
               fill=colours[0], width=3)

cv.create_text(canvas_width / 2,
               canvas_height / 2,
               text="Python")
window.mainloop()
