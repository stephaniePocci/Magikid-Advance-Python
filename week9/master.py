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


# IMAGE

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("PhotoImage on Canvas")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Load the image
photo = tk.PhotoImage(file="./example.png")

# Add the image to the canvas
canvas.create_image(200, 150, image=photo, anchor=tk.CENTER)

root.mainloop()


# TIMER

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