import tkinter as tk
import time
import random  # 添加 random 库

'''Step1:设置窗口(设置游戏画布)'''

window = tk.Tk()

canvas_width = 800
canvas_height = 800

canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="#006400")
canvas.pack()

window.update()  # 刷新页面

'''Step2: 在画布上创建一个小球'''
ball1 = canvas.create_oval((0, 0), (40, 40), fill="red")

# 将小球放进画布canvas中，移动小球到指定的初始位置
canvas.move(ball1, 330, 380)

'''Step 3: 设置两个变量作为小球的初始移动方式'''
start_x = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
random.shuffle(start_x)  # 将列表混排(顺序打乱)

ball1_x = start_x[0]
# ball1_x = 0  # 垂直
ball1_y = -5  # 向上


'''Step 4: 定义小球的移动方向和速度'''
def draw():
    global ball1_x
    global ball1_y
    canvas.move(ball1, ball1_x, ball1_y)
    pos1 = canvas.coords(ball1)  # 将小球的坐标(4个数字的元祖)赋值给变量 pos1
    if pos1[1] <= 0:
        ball1_y = 5
    if pos1[3] >= canvas_height:
        ball1_y = -5
    '''Step 5:添加 x 反弹条件'''
    if pos1[0] <= 0:
        ball1_x = -ball1_x
    if pos1[2] >= canvas_width:
        ball1_x = -ball1_x


'''Step6:创建主循环程序，让程序运行'''
while True:  # 永久循环
    draw()
    window.update()  # 屏幕刷新
    time.sleep(0.01)

tk.mainloop()
