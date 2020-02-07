import tkinter as tk
import time
import random
import sys
import csv
import subprocess

x = 0
y = 0
i = 0
args = sys.argv
name = str(args[1])
exp_code = int(args[2])#0:inner_plus_trial, 1:inner_minus_trial, 2:robot_plus_trial, 3:robot_minus_trial, 4:noise_trial

#記録用CSVファイル作成######################
f = open(name+"/"+str(exp_code)+"ball_number.csv", 'a')
writer = csv.writer(f, lineterminator="\n")
list=[]

g = open(name+"/"+str(exp_code)+"inner_number.csv", 'a')
writer_inner = csv.writer(g, lineterminator="\n")
list_inner=[]

trial = 15 + random.randrange(11)#赤丸の出現回数、15以上25以下
inner = 5 + random.randrange(6)#inner number5以上10以下

list.append(trial)
writer.writerow(list)

list_inner.append(inner)
writer_inner.writerow(list_inner)
##########################################

window = tk.Tk()
canvas = tk.Canvas(window, width = 1400, height = 1400)##キャンバスの大きさを決定
canvas.create_oval(200, 200, 100, 100, fill='red', tags='ball')##玉の大きさx,y,位置x,y
canvas.pack()

def move():
    global x
    global y
    global i
    canvas.delete('ball')
    canvas.create_oval(200+x, 200+y, 100+x, 100+y, fill='red', tags='ball')
    i = i + 1
    temx = x
    temy = y
    while((x==temx)&(y==temy)):
        x =350*random.randrange(4)
        y =350*random.randrange(4)

    if(i<trial):
        window.after(500, move)
    if(i==inner):##inner回数目の玉出現時にinner刺激
        if(exp_code==0):
            cmd = "python sub.py "+str(name)+" "+str(inner+2)
            pro = subprocess.Popen(cmd)
        if(exp_code==1):
            cmd = "python sub.py "+str(name)+" "+str(inner)
            pro = subprocess.Popen(cmd)
        if(exp_code==2):
            cmd = "python sub.py robot robot"+str(inner+2)
            pro = subprocess.Popen(cmd)
        if(exp_code==3):
            cmd = "python sub.py robot robot"+str(inner)
            pro = subprocess.Popen(cmd)
        if(exp_code==4):
            cmd = "python sub.py robot noise"
            pro = subprocess.Popen(cmd)

window.after(500, move)
window.geometry('-2100+350')##キャンバスの位置を決定
tk.mainloop()
