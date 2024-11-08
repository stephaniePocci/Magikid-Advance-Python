from tkinter import *

window = Tk()

window.title("Listbox2")

window.geometry("400x300+1000+150")


lb = Listbox(window,
             selectmode=BROWSE)  


list_items = ["item1", "item2", "item3", "item4"]


for item in list_items:
    lb.insert(END, item)  


lb.insert(ACTIVE, "ACTIVE, 在开始添加")


lb.insert(1, "First")


lb.insert(END, ["Hello, world!", "Hello, Leo!"])


lb.insert(END, [1, 2, 3, 4])


lb.delete(0, 1)


lb.select_set(3, 4)


lb.select_clear(3)


print(lb.size())


print(lb.get(2, 3))


print(lb.curselection())


print(lb.selection_includes(3))

lb.pack()

window.mainloop()


