import random
import csv
import subprocess
import time
import cv2

from record import MakeWavFile
from png import show,show_str

##音質の違い
inner_plus_trial = 10
inner_minus_trial = 10
robot_plus_trial = 10
inner_minus_trial = 10
noise_trial = 10
list_exp = [inner_plus_trial,inner_minus_trial,robot_plus_trial,inner_minus_trial,noise_trial]

if __name__ == '__main__':
    trial = 50 #試行回数
    name = "yamaoka" #被験者の名前
    list = []

    for i in range(trial):
            exp_code = random.randrange(5)##0:inner_plus_trial, 1:inner_minus_trial, 2:robot_plus_trial, 3:robot_minus_trial, 4:noise_trial
            while(list_exp[exp_code]==0):
                exp_code = random.randrange(5)
            list_exp[exp_code] = list_exp[exp_code] - 1
            print(exp_code)


            show_str("start")
            time.sleep(2)
            cv2.destroyAllWindows()
            cmd = "python gui.py " + name + " " + str(exp_code)##python gui.py name exp_code{0,1,2,3}でgui実行
            pro = subprocess.Popen(cmd)
            time.sleep(15)
            pro.terminate()

            MakeWavFile(name+"/record/"+str(exp_code)+"-"+str(10-list_exp[exp_code]) + ".wav",3)
            show_str("answer")
            time.sleep(2)
            cv2.destroyAllWindows()
