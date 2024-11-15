from tkinter import *

# Step1: Create a main window named 'window'
window = Tk()

# Step2: Set window title named 'My Window'
window.title('Listbox')

# Step3: Set window size and position
window.geometry('400x300+2000+150')

list_items = ['item1', 'item2', 'item3', 'item4']

# Step4: Create a variable as the value of the listbox
var = StringVar()
var.set(list_items)  # Set value for variable 'var'

# Step5: Create a 'Listbox' widgets
"""
Selectmode	| Description                                   | Selection Behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SINGLE	    | Single item selection	                        | Only one item at a time
BROWSE	    | Single item with dragging capability	        | One item at a time, draggable
MULTIPLE	| Multiple independent item selections	        | Multiple items, toggle with clicks
EXTENDED	| Contiguous and non-contiguous item selections	| Use Shift for range, Control for toggle
"""
lb = Listbox(window, listvariable=var, selectmode=MULTIPLE, font=('Arial', 16))

lb.pack()

# Step6: insert
# loop insert
list_items = ['item5', 'item6', 'item7', 'item8']

for item in list_items:
    lb.insert(END, item)  

# insert to active selection
# lb.insert(ACTIVE, "ACTIVE, 在开始添加")

# insert at index 1, shift everything else 1 down
lb.insert(1, "First")

# insert at the end, this is considered one entry
# lb.insert(END, ["Hello, world!", "Hello, Leo!"])

# Step 7: delete
# deletes items from index 0 to 1, so it will delete 0 and 1
lb.delete(0, 1)

# Step 8: select
lb.select_set(3, 4)
lb.select_set(ACTIVE)
lb.select_set(3)

# Step 9: select clear

# clears entry at 3
lb.select_clear(3)
# clears entries from index 1 to 2
lb.select_clear(1, 2)

# Prints the total number of items in the Listbox.
print(lb.size())

# Retrieves the items at indices 2 and 3 (inclusive) and prints them.
print(lb.get(2, 3))

# Prints the currently selected items' indices in the Listbox.
print(lb.curselection())

# Checks if the item at index 3 is currently selected and prints True or False.
print(lb.selection_includes(3))

entry = Entry(window, show=None, font=('Arial', 16))  # Show in plaintext
entry.pack()

def add_item():
    item = entry.get()
    lb.insert(END, item)

Button(window, text="ADD", command=add_item, font=('Arial', 16)).pack()

# Step: Set the main window loop
window.mainloop()


