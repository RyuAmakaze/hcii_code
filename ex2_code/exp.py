import random
import csv
import subprocess
import time
import cv2

from record import MakeWavFile
from png import show,show_str

##音質の違い
inner_plus_trial = 15
inner_minus_trial = 15
robot_plus_trial = 15
inner_minus_trial = 15
noise_trial = 30
list_exp = [inner_plus_trial,inner_minus_trial,robot_plus_trial,inner_minus_trial,noise_trial]

if __name__ == '__main__':
    trial = 90 #試行回数
    name = "yamaoka" #被験者の名前
    exp_order_list = []

    for i in range(trial):
            print("")
            print("************************************************")
            exp_code = random.randrange(6)
            if(exp_code==5):
                exp_code = 4
            ##0:inner_plus_trial, 1:inner_minus_trial, 2:robot_plus_trial, 3:robot_minus_trial, 4:noise_trial
            while(list_exp[exp_code]==0):
                exp_code = random.randrange(5)
            list_exp[exp_code] = list_exp[exp_code] - 1
            print("exp_code : " + str(exp_code))
            exp_order_list.append(exp_code)


            show_str("start")
            time.sleep(1)
            cv2.destroyAllWindows()
            cmd = "python gui.py " + name + " " + str(exp_code)##python gui.py name exp_code{0,1,2,3}でgui実行
            pro = subprocess.Popen(cmd)
            time.sleep(13)
            pro.terminate()

            cmd2 = "python show.py"
            pro = subprocess.Popen(cmd2)
            if(exp_code==4):
                MakeWavFile(name+"/record/"+str(exp_code)+"-"+str(30-list_exp[exp_code]) + ".wav",3)
            else:
                MakeWavFile(name+"/record/"+str(exp_code)+"-"+str(15-list_exp[exp_code]) + ".wav",3)
            pro.terminate()

    f = open(name+"/exp_order_list.csv", 'a')
    writer = csv.writer(f, lineterminator="\n")
    writer.writerow(exp_order_list)
    print("実験終了")
