"""
.pack() Manager

The .pack() method arranges widgets in blocks, which can be stacked vertically or placed side-by-side. The attributes below adjust its behavior:

    side=RIGHT, LEFT, TOP, BOTTOM: Specifies which side of the parent widget the child widget should attach to.
        TOP (default): Widgets are stacked vertically from the top.
        LEFT: Widgets stack horizontally from the left.
        RIGHT: Widgets stack horizontally from the right.
        BOTTOM: Widgets stack vertically from the bottom.

    fill: Determines whether the widget should stretch to fill the space.
        NONE (default): No filling.
        X: Expands horizontally.
        Y: Expands vertically.
        BOTH: Expands both horizontally and vertically.

    padx, pady: Adds external padding around the widget.
        padx: Horizontal space to the left and right of the widget.
        pady: Vertical space above and below the widget.

    ipadx, ipady: Adds internal padding (inside the widget).
        ipadx: Horizontal space inside the widget.
        ipady: Vertical space inside the widget.

    expand: When set to True, it makes the widget expand to fill any extra space in the parent.

    anchor: Determines the position of the widget within its allocated space.
        Values can be compass directions: N, S, E, W, NE, NW, SE, SW, and CENTER (default).

.place() Manager

The .place() method positions widgets using absolute or relative coordinates.

    x: Horizontal pixel position from the top-left corner of the parent widget.
    y: Vertical pixel position from the top-left corner of the parent widget.
    width: Sets a specific width for the widget in pixels.
    height: Sets a specific height for the widget in pixels.
    relx: Relative horizontal position (as a fraction of the width of the parent).
    rely: Relative vertical position (as a fraction of the height of the parent).
    relwidth: Relative width as a fraction of the parent's width.
    relheight: Relative height as a fraction of the parent's height.

.grid() Manager

The .grid() method positions widgets in a table-like layout, with rows and columns.

    row: Specifies the row of the grid where the widget will be placed.
    column: Specifies the column of the grid where the widget will be placed.
    rowspan: Number of rows the widget should span vertically.
    columnspan: Number of columns the widget should span horizontally.
    sticky: Aligns the widget within the cell (similar to anchor in .pack()).
        Values are compass directions: N, S, E, W (e.g., sticky=N+W aligns to the top-left corner).
    padx, pady: Adds external padding around the widget in the grid cell.
        padx: Horizontal space in the grid cell.
        pady: Vertical space in the grid cell.

.winfo_screenwidth()

    Returns: The width of the screen in pixels.
        Useful for making your application dynamically adapt to the screen size.


"""

# CHALLENGE
'''
1. make a calculator with a label for the sum, and buttons for + - and 0-9
2. write functions to handle + or - logic
3. add submit button to do the math
4. add functionality to chain more operations
5. add / and *
6. throw errors for dividing by zero
'''

from tkinter import *

window = Tk()

window.title("Frame Demo")
window.geometry("400x900+2000+100")
Label(window, text="Main window",
      bg='blue', fg='white',
      font=('Arial', 16)).pack()

# Create a main frame
frame_master = Frame(window, bg='red')
frame_master.pack()
Label(frame_master, text="number", bg='green', font=('Arial', 26)).pack()


# Create a left subframe in the main frame
frame_left = Frame(frame_master)
frame_left.pack(side=LEFT)
Button(frame_left,
      text="1", bg='red').grid(row=0, column=0)
Button(frame_left,
      text="2", bg='blue').grid(row=0, column=1)
Button(frame_left,
      text="3", bg='green').grid(row=0, column=2)
Button(frame_left,
      text="4", bg='purple').grid(row=1, column=0)
Button(frame_left,
      text="5", bg='yellow').grid(row=1, column=1)
Button(frame_left,
      text="6", bg='pink').grid(row=1, column=2)
Button(frame_left,
      text="7", bg='orange').grid(row=2, column=0)
Button(frame_left,
      text="8", bg='brown').grid(row=2, column=1)
Button(frame_left,
      text="9", bg='white').grid(row=2, column=2)


# Create a right subframe in the main frame
frame_right = Frame(frame_master, bg='black')
frame_right.pack(side=RIGHT)
Label(frame_right,
      text="+", bg='pink').pack()
Label(frame_right,
      text="-", bg='pink').pack()
Label(frame_right,
      text="/", bg='pink').pack()
Label(frame_right,
      text="*", bg='pink').pack()
Label(frame_right,
      text="Enter", bg='pink').pack()

window.mainloop()
