import tkinter as tk
import time

'''Step1:设置窗口(设置游戏画布)'''

window = tk.Tk()

canvas = tk.Canvas(window, width=700, height=800, bg="#006400")
canvas.pack()

window.update()  # 刷新页面

'''Step2: 在画布上创建一个小球'''

# 在 canvas 画布上绘制一个(有颜色的)小球
ball1 = canvas.create_oval((0, 0), (40, 40), fill="red")
ball2 = canvas.create_oval((0, 0), (40, 40), fill="yellow")

# 将小球放进画布canvas中，设置小球的初始位置
canvas.move(ball1, 330, 600)
canvas.move(ball2, 330, 200)


# 定义小球的移动方向和速度
def draw():
    canvas.move(ball1, 0, -5)  # 红球向上移动
    canvas.move(ball2, 0, 5)  # 黄球向下移动


'''Step3:创建主循环程序，让程序运行'''

while True:  # 永久循环
    draw()
    window.update()  # 屏幕刷新
    time.sleep(0.01)

tk.mainloop()
