"""
### Scale

Scale(
    label #text
    from_=0, to=10, # Define the range of the scale.
    orient=HORIZONTAL | VERTICAL,
    length=300, # width in pixels
    showvalue=1 | 0,  # Whether to display the current value
    tickinterval=2,  # Displays tick marks at intervals along the scale.
    resolution=1,  # The accuracy is 0.01, Sets the smallest increment by which the scale’s value can change.
    activebackground='green' # when hover
    command #command
)

scale.set("initial")


### PhotoImage

PhotoImage 


### Canvas

cv = Canvas(window, width, height)

cv.create_line(
    x1, y1,  # Coordinates of the start and end points (can have more points for connected lines).
    x2, y2, 
    fill, 
    width # thickness of line
    arrow # none, first, last, both
    arrowshape # Tuple for arrow dimensions (length, width, wing width).
    dash # Pattern for dashed lines (e.g., (5, 2) for 5-pixel dash, 2-pixel space).
)

cv.create_rectangle(
    x1, y1, # Coordinates of the top-left 
    x2, y2, # bottom-right corners of the rectangle.
    fill, 
    width # thickness of line
    dash # Pattern for dashed lines (e.g., (5, 2) for 5-pixel dash, 2-pixel space).
)

canvas.create_image(
    x, y, # Anchor point coordinates for the image.
    image
    anchor # center, n, s, e, w, nw, ne, sw, se
    tags
)

canvas.create_text(
    x, y, # Coordinates of the text's anchor point.
    text
    font
    fill
    anchor # center, n, s, e, w, nw, ne, sw, se
    justify
    width # width of the text box
    tags
)

canvas.move("red_items", 20, 0)
canvas.delete("red_items") # Tags provide a way to reference canvas items without needing their specific IDs


"""
# scale
from tkinter import *

window = Tk()

window.title("Scale Practice")

window.geometry('400x300')

lbl = Label(window,
            bg='green', fg='white',
            width=20, height=2,
            text="Empty")
lbl.pack()

# var = StringVar()


def print_selection(a):    
    lbl.config(text="You have selected " + a)
    # print(var.get())
    # print(v)


scale = Scale(window,
              label="try me",
              from_=0, to=10,
              orient=HORIZONTAL,
              length=300,
              showvalue=1,  # Whether to display the current value
              tickinterval=2,  # scale is 2
              resolution=1,  # The accuracy is 0.01
              command=print_selection)
scale.pack()

# canvas

canvas_width = 200
canvas_height = 100

cv = Canvas(window,
            width=canvas_width, height=canvas_height)
cv.pack()

cv.create_rectangle(50, 20, 150, 80, fill="#4169E1")
cv.create_rectangle(65, 35, 135, 65, fill="yellow")
cv.create_line(0, 0, 50, 20, fill="#4169E1", width=3)
cv.create_line(0, 100, 50, 80, fill="#4169E1", width=3)
cv.create_line(150,20, 200, 0, fill="#4169E1", width=3)
cv.create_line(150, 80, 200, 100, fill="#4169E1", width=3)



# IMAGE


# Create a Canvas widget
canvas = Canvas(window, width=400, height=300, bg="white")
canvas.pack()

# Load the image
<<<<<<< HEAD
photo = tk.PhotoImage(file="./example.png")
=======
# photo = PhotoImage(file="example.gif")
>>>>>>> 9bc29e4974e58b4d7106c850ff00121d448cba80

# Add the image to the canvas
# canvas.create_image(200, 150, image=photo, anchor=CENTER)



# TIMER

<<<<<<< HEAD
# import tkinter as tk

# def update_timer():
#     global counter
#     counter += 1
#     label.config(text=f"Timer: {counter} seconds")
#     root.after(1000, update_timer)  # Call this function again in 1 second

# root = tk.Tk()
# counter = 0
# label = tk.Label(root, text="Timer: 0 seconds")
# label.pack()

# update_timer()  # Start the timer
# root.mainloop()
=======
def update_timer():
    global counter
    counter += 1
    countlb.config(text=f"Timer: {counter} seconds")
    window.after(1000, update_timer)  # Call this function again in 1 second

counter = 0
countlb = Label(window, text="Timer: 0 seconds")
countlb.pack()

update_timer()  # Start the timer
window.mainloop()
>>>>>>> 9bc29e4974e58b4d7106c850ff00121d448cba80
