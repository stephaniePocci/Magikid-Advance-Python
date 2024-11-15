from tkinter import *

window = Tk()

window.title("Checkbutton Demo")

lbl = Label(window,
            text="This is a multiple option：",
            font=('Arial', 16))
lbl.pack()

cb1 = Checkbutton(window,
                  text="Python",
                  font=('Arial', 16))
cb1.pack()

cb2 = Checkbutton(window,
                  text="JavaScript",
                  font=('Arial', 16))
cb2.pack()

cb3 = Checkbutton(window,
                  text="C++",
                  font=('Arial', 16))
cb3.pack()

window.mainloop()


'''
常用参数：
onvalue       指定Checkbutton处于On状态时的值，如，onvalue=“valueX”
offvalue      指定Checkbutton处于Off状态时的值
variable      控制变量，跟踪Checkbutton的状态，On(1)，Off(0)
bd            设置Checkbutton的边框大小;bd(bordwidth)缺省为1或2个像素
textvariable  设置Checkbutton的textvariable属性，文本内容变量
padx          标签水平方向的边距, 默认为1像素
pady          标签竖直方向的边距, 默认为1像素.
justify       标签文字的对齐方向, 可选值为 RIGHT, CENTER, LEFT, 默认为 Center
relief        指定外观装饰边界附近的标签,默认是平的,可以设置的参数：flat、groove、raised、ridge、solid、sunken
wraplength    将此选项设置为所需的数量限制每行的字符,数默认为0
state         设置组件状态;正常(normal),激活(active),禁用(disabled)
selectcolor   设置选中区的颜色
selectimage   设置选中区的图像，选中时会出现
'''

'''
常用方法：
deselect()  清除（关闭）复选框。
flash()     在复选按钮的活动颜色和正常颜色之间闪烁几次，但保持其开始时的状态。
invoke()    您可以调用此方法来获得与用户单击复选框以更改其状态时将发生的操作相同的操作。
select()    设置（打开）复选按钮。
toggle()    如果选中该复选框，则将其清除；如果清除，则对其进行设置。
deselect()  清除（关闭）复选框。
toggle()    如果选中该复选框，则将其清除；如果清除，则对其进行设置。
'''
