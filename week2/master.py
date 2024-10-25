# Pack and Label Stuff
from tkinter import *

leo = Tk()

leo.title('Test')

leo.resizable(0, 0)

leo.geometry('400x300+1000+150')

lbl1 = Label(leo, text='Test 1')
lbl1.pack(anchor=CENTER)
lbl2 = Label(leo, text='Test 2')
lbl2.pack(side=LEFT)
lbl3 = Label(leo, text='Test 3')
lbl3.pack(side=BOTTOM)



Label(leo, text='Test').pack(side=RIGHT, anchor=CENTER)

# Global




window.title("Label and Button")

window.geometry('400x300')

lbl = Label(window, text="You click me!", font=('Arial', 20), fg='white', bg='blue', height=2, width=16)
lbl.pack()

i = 0  


def click_me():
    global i  
    i = i + 1
    print("You click me " + str(i) + " time!")


btn = Button(window, text='Click Me', height=2, width=12, command=click_me)
btn.pack()

window.mainloop()

# Strings

from tkinter import *

window = Tk()
window.title("Label and Button")
window.geometry('400x300')

# Set the content of the label tag as a character type, and use var to receive the
# outgoing content of the Click Me function to display on the label；
var = StringVar()

lbl = Label(window, textvariable=var, font=('Arial', 20), fg='white',
            bg='blue', height=2, width=20)
lbl.pack()

i = 0

def click_me():
    global i
    i = i + 1
    var.set("You click me " + str(i) + " time!")

btn = Button(window, text='Click Me', height=2, width=12, command=click_me)
btn.pack()

window.mainloop()

Button(window, text='Click Me', height=2, width=12, command=click_me).pack()





# Recursive function
def reduce_to_zero(num):
    print(num)

    # Base Case
    if num == 0:
        return
    
    num = num - 1

    #Recursive Case
    reduce_to_zero(num)

# Start the recursive function
reduce_to_zero(10)


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_bst(node: TreeNode) -> None:
    if node is None:
        return
    
    inorder_bst(node.left)
    print(node.value)
    inorder_bst(node.right)





