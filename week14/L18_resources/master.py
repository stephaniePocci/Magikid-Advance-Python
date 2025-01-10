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