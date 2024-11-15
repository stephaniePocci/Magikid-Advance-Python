# initialize our window
from tkinter import *

window = Tk()

window.geometry('400x300+2000+150')

# create a list of items, for me its food
list_items = ["apple", "orange", "cherry", "mango"]
# Storing our list to a string variable
food = StringVar()
food.set(list_items)
# SINGLE, BROWSE, MULTIPLE, EXTENDED
lb = Listbox(window, listvariable=food, selectmode=BROWSE)
lb.pack()

lb.insert(END, "Dragonfruit")
lb.insert(1, "cantalope")

new_fruits = ["watermelon", "strawberry"]

for fruit in new_fruits:
    lb.insert(END, fruit)
# apple cantalope orange cherry mango dragonfruit watermelon strawberry

lb.delete(0)
# cantalope orange cherry mango dragonfruit watermelon strawberry
lb.delete(1,3)
# cantalope dragonfruit watermelon strawberry

lb.select_set(1,2)

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

window.mainloop()