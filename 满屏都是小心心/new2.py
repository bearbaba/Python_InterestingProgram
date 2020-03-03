import tkinter as tk
import turtle as tr
import random


def showHeart():
    global screenheight, screenwidth
    tr.setup(width=1.0, height=1.0)
    tr.pensize(1)
    tr.fillcolor("pink")
    tr.pencolor("red")
    tr.speed(10)
    while(True):
        tr.hideturtle()
        tr.pendown()
        line = random.randint(50, 100)
        x = random.randrange(-screenwidth/2+100, screenwidth/2-100)
        y = random.randrange(-screenheight/2, screenheight/2-200)
        tr.begin_fill()

        tr.left(45)
        tr.forward(line)
        tr.circle(line/2, 180)
        tr.right(90)
        tr.circle(line/2, 180)
        tr.forward(line)
        tr.left(45)
        tr.end_fill()
        tr.penup()
        tr.goto(x, y)


def exit_():
    root.destroy()


root = tk.Tk()
root.geometry("500x300")
root.wm_title("满屏都是小心心")

screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

frame2 = tk.Frame(root)
frame1 = tk.Frame(frame2)
button1 = tk.Button(frame1, text="是", command=showHeart,
                    activeforeground='red', font=("正楷", "12"))
button2 = tk.Button(frame1, text="否", command=exit_,
                    activeforeground='red', font=("正楷", 12))
label1 = tk.Label(frame2, text="点击生成心心", font=("正楷", "18"))
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)

label1.grid(row=0)
frame1.grid(row=1)

frame2.grid(row=0, padx=200, pady=120)
tk.mainloop()
