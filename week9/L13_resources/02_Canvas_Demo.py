from tkinter import *

window = Tk()

canvas = Canvas(window, width=400, height=200)
canvas.pack()

canvas.create_line((0, 100), (400, 100),
                   width=5, fill="#4169E1")
canvas.create_text(200, 80, text="draw a straight line", font=("Arial", 20))

a = canvas.coords()

print(a)

mainloop()


'''
Exclusive function：
create_arc       
create_bitmap    bitmap= BitmapImage(file = filepath)
create_image     (x,y,image,anchor); image= PhotoImage(file="../xxx/xxx.gif") 
create_line      
create_oval      
create_polygon   
create_rectangle 
create_text      font=("Arial", 8)，font=("Helvetica 16 bold italic")
create_window    
delete           
itemconfig       
move             
coords(ID)       
'''
