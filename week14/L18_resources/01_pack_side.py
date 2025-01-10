from tkinter import *

window = Tk()

window.title("pack_side")

window.geometry('400x300')

Label(window, text=".pack(side=TOP)").pack(side=TOP)
Label(window, text=".pack(side=BOTTOM)",
      bg="red", fg="white").pack(side=BOTTOM)
Label(window, text=".pack(side=LEFT)",
      bg="blue", fg="white").pack(side=LEFT)
Label(window, text=".pack(side=RIGHT)",
      bg="green", fg="white").pack(side=RIGHT)

window.mainloop()


'''
pack()常用参数/选项：
side      默认值是 TOP ，还可以是 LEFT 、RIGHT 、BOTTOM，如 pack(side=LEFT) ；
anchor    默认值是CENTER，还可以是 N、NE、E、SE、S、WS、W、NW（东南西北中）；
expand    是否填充父组件的额外空间，默认值是 False ；
fill      指定填充 pack 分配的空间。默认值是 NONE ，表示保持子组件的原始尺寸。还可以是 "x"（水平填充）、"y"（垂直填充）和 "both"（水平和垂直填充）
in_       将组件放到该选项指定的组件中，指定的组件必须是该组件的父组件；
ipadx     指定水平方向上的内边距；
ipady     指定垂直方向上的内边距；
padx      指定水平方向上的外边距；
pady      指定垂直方向上的外边距；    
--------------------------------------------------------------------------------------------------------------------------------
pack常用方法：            
pack_configure(**options)    跟 pack() 一样；
pack_forget()                将组件从屏幕中“删除”，并没有销毁该组件，只是看不到了，可以通过 pack 或其他布局管理器显示已“删除”的组件；
pack_info()                  以字典的形式返回当前 pack 的选项；
pack_propagate(flag)         如果开启，父组件会自动调节尺寸以容纳所有子组件。默认值是开启（flag = True），该方法仅适用于父组件；
pack_slaves()                以列表的形式返回该组件的所有子组件；
'''