import tkinter as tk
import time
import random
x = 0
i = 0
trial = 15 + random.randrange(10)
window = tk.Tk()
canvas = tk.Canvas(window, width = 800, height = 800)
canvas.create_oval(200, 200, 0, 0, fill='red', tags='ball')
canvas.pack()

def move():
    global x
    global i
    canvas.delete('ball')
    canvas.create_oval(200+x, 200+x, 0+x, 0+x, fill='red', tags='ball')
    i = i + 1
    tem = x
    while(x==tem):
        x =200*random.randrange(4)

    if(i<trial):
        window.after(500, move)

window.after(500, move)
window.geometry('-2700+900')
tk.mainloop()
