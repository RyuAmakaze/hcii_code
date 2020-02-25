import tkinter as tk
import time
import random
import sys
import csv
import subprocess
from tkinter import font
#from test import open

x = 0
y = 0
i = 0
flag = 0
args = sys.argv
name = str(args[1])
exp_code = int(args[2])#0:inner_plus_trial, 1:inner_minus_trial, 2:robot_plus_trial, 3:robot_minus_trial, 4:noise_trial

#記録用CSVファイル作成######################
list=[]
list_inner=[]
x_list=[]
y_list=[]
kind_list = []
time_list = []

red_i = 0##赤丸の出現回数が答え
blue_i = 0
inner = 6 + random.randrange(5)#inner number6以上10以下
#iiner2 = 8 + random.randrange(8)#inner
print("stimu number : " + str(inner))

##########################################

window = tk.Tk()
canvas = tk.Canvas(window, width = 1400, height = 1400)##キャンバスの大きさを決定
##canvas.create_oval(200, 200, 100, 100, fill='red', tags='ball')##玉の大きさx,y,位置x,y
canvas.pack()

def move():
    global x,y,i,blue_i,red_i,flag,trial,inner
    global x_list,y_list,list,list_inner

    canvas.delete('ball')##以前の玉を消す
    i = i + 1##iがtrial以下ならば、玉の出現を続ける。

    ##丸の出現場所を決める
    temx = x
    temy = y
    x =350*random.randrange(4)
    y =350*random.randrange(4)
    while((x==temx)&(y==temy)):
        x =350*random.randrange(4)
        y =350*random.randrange(4)

    ##x,yの位置座標保存用
    x_list.append(x)
    time_list.append(time.time())
    y_list.append(y)

    ##青丸か赤丸かの認知タスクを加える。
    flag2 = random.randrange(4)
    if(red_i==inner):##刺激を与えるときは必ず赤丸を出現させる
        flag2 = 1
    if(flag2==3):
        if(blue_i<15-inner-3):
            canvas.create_rectangle(200+x, 200+y, 100+x, 100+y, fill='red', tags='ball')
            blue_i = blue_i + 1
            kind_ball = 0#出現図形の記録用
        else:
            canvas.create_oval(200+x, 200+y, 100+x, 100+y, fill='red', tags='ball')
            red_i = red_i + 1
            kind_ball = 1

    if(flag2<3):
        if(red_i<=15):
            canvas.create_oval(200+x, 200+y, 100+x, 100+y, fill='red', tags='ball')
            red_i = red_i + 1
            kind_ball = 1
        else:
            canvas.create_rectangle(200+x, 200+y, 100+x, 100+y, fill='red', tags='ball')
            blue_i = blue_i + 1
            kind_ball = 0
    kind_list.append(kind_ball)

    ##音響刺激の選択、および再生
    if((red_i==inner)&(flag==0)):##inner回数目の赤玉出現時にinner刺激
        flag = 1
        #print("iiner")
        if(exp_code==0):
            cmd = "python sub.py "+str(name)+" "+str(inner)
            pro = subprocess.Popen(cmd)
        if(exp_code==1):
            cmd = "python sub.py robot robot"+str(inner)
            pro = subprocess.Popen(cmd)
            #print("inner")
            #open("robot/robot" + str(inner))
        if(exp_code==2):
            cmd = "python sub.py robot noise"
            pro = subprocess.Popen(cmd)


    if(i<15):
        window.after(400, move)
    else:##一試行の終了
        #canvas.delete('ball')
        #font1 = font.Font(family="Times",size=50,weight="bold")
        #label1 = tk.Label(window,text="Answer",font=font1)
        #label1.place(x=500,y=200)
        #time.sleep(2)
        #print("test")

        print("correct number : " + str(red_i))
        list.append(red_i)
        list_inner.append(inner)

        xl = open(name+"/"+str(exp_code)+"x_pos.csv", 'a')
        x_writer = csv.writer(xl, lineterminator="\n")

        yl = open(name+"/"+str(exp_code)+"y_pos.csv", 'a')
        y_writer = csv.writer(yl, lineterminator="\n")

        timel = open(name+"/"+str(exp_code)+"time.csv", 'a')
        time_writer = csv.writer(timel, lineterminator="\n")

        f = open(name+"/"+str(exp_code)+"correct_number.csv", 'a')
        writer = csv.writer(f, lineterminator="\n")

        g = open(name+"/"+str(exp_code)+"inner_number.csv", 'a')
        writer_inner = csv.writer(g, lineterminator="\n")

        kind = open(name+"/"+str(exp_code)+"kind_ball.csv", 'a')
        kind_writer = csv.writer(kind, lineterminator="\n")

        writer.writerow(list)
        writer_inner.writerow(list_inner)
        x_writer.writerow(x_list)
        y_writer.writerow(y_list)
        time_writer.writerow(time_list)
        kind_writer.writerow(kind_list)

window.after(400, move)
window.geometry('-2100+350')##キャンバスの位置を決定
tk.mainloop()
