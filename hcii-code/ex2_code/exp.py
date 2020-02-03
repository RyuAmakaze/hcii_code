import random
import csv
import subprocess
import time
import cv2

from record import MakeWavFile
from png import show,show_str

if __name__ == '__main__':
    trial = 20 #試行回数
    name = "yamaoka" #被験者の名前
    kind_exp = 0 # 0:inner read, 1:robot voice , 2:white noise

    for i in range(trial):
            show_str("start")
            time.sleep(3)
            cv2.destroyAllWindows()
            time.sleep(3)
            #cmd = "python gui.py "
            #pro = subprocess.Popen(cmd)
