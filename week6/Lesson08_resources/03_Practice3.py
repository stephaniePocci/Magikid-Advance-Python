from tkinter import *

# Step1: Create a main window named 'window'
window = Tk()

# Step2: Set window title named 'My Window'
window.title('Listbox')

# Step3: Set window size and position
window.geometry('400x300+1000+150')


var1 = StringVar()  
lbl = Label(window, bg='green', fg='yellow',
            font=('Arial', 12), width=10, textvariable=var1)
lbl.pack()



def print_selection():
    value = lb.get(lb.curselection())  
    var1.set(value)  



btn1 = Button(window, text='print selection',
              width=15, height=2, command=print_selection)
btn1.pack()


var2 = StringVar()
var2.set((1, 2, 3, 4))  


lb = Listbox(window, listvariable=var2)  


list_items = [11, 22, 33, 44]
for item in list_items:
    lb.insert('end', item)  

lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2) 

lb.pack()  

window.mainloop()
