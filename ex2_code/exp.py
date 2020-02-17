import random
import csv
import subprocess
import time
import cv2

from record import MakeWavFile
from png import show,show_str

##音質の違い,3条件
inner_trial = 30
robot_trial = 30
noise_trial = 30
list_exp = [inner_trial,robot_trial,noise_trial]

if __name__ == '__main__':
    trial = 30 #試行回数
    name = "yamaoka" #被験者の名前
    exp_order_list = []

    for i in range(trial):
            print("")
            print("************************************************")
            exp_code = 1#random.randrange(3)

            ##0:inner_trial,1:robot_trial,4:noise_trial
            while(list_exp[exp_code]==0):
                exp_code = random.randrange(3)
            list_exp[exp_code] = list_exp[exp_code] - 1
            print("exp_code : " + str(exp_code))
            exp_order_list.append(exp_code)


            show_str("start")
            time.sleep(1)
            cv2.destroyAllWindows()
            cmd = "python gui.py " + name + " " + str(exp_code)##python gui.py name exp_code{0,1,2,3}でgui実行
            pro = subprocess.Popen(cmd)
            time.sleep(14)
            pro.terminate()

            cmd2 = "python show.py"
            pro = subprocess.Popen(cmd2)
            MakeWavFile(name+"/record/"+str(exp_code)+"-"+str(30-list_exp[exp_code]) + ".wav",2)
            pro.terminate()

    f = open(name+"/exp_order_list.csv", 'a')
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(exp_order_list)
    print("実験終了")
