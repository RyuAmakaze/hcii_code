import tkinter as tk
import time
import random
import sys
import csv
import subprocess

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

trial = 10 + random.randrange(11)#赤丸の出現回数、15以上25以下
inner = 5 + random.randrange(6)#inner number5以上10以下

list.append(trial)
list_inner.append(inner)

red_i = trial##赤丸の出現回数が答え
blue_i = 25 - trial
print("correct number : " + str(trial))
print("stimu number : " + str(inner))

x_list=[]
y_list=[]
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

    ##青丸か赤丸かの認知タスクを加える。
    if((random.randrange(3)==0)&(blue_i!=0)):
        canvas.create_oval(200+x, 200+y, 100+x, 100+y, fill='blue', tags='ball')
        blue_i = blue_i - 1
    else:
        canvas.create_oval(200+x, 200+y, 100+x, 100+y, fill='red', tags='ball')
        red_i = red_i - 1

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
    y_list.append(y)

    ##音響刺激を特徴づける。
    if((red_i==(trial-inner))&(flag==0)):##inner回数目の赤玉出現時にinner刺激
        flag = 1
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

    if(i<25):
        window.after(500, move)
    else:
        xl = open(name+"/"+str(exp_code)+"x_pos.csv", 'a')
        x_writer = csv.writer(xl, lineterminator="\n")
        yl = open(name+"/"+str(exp_code)+"y_pos.csv", 'a')
        y_writer = csv.writer(yl, lineterminator="\n")
        f = open(name+"/"+str(exp_code)+"correct_number.csv", 'a')
        writer = csv.writer(f, lineterminator="\n")
        g = open(name+"/"+str(exp_code)+"inner_number.csv", 'a')
        writer_inner = csv.writer(g, lineterminator="\n")

        writer.writerow(list)
        writer_inner.writerow(list_inner)
        x_writer.writerow(x_list)
        y_writer.writerow(y_list)
window.after(500, move)
window.geometry('-2100+350')##キャンバスの位置を決定
tk.mainloop()
