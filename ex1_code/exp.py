from msvcrt import getch
import random
import csv
import subprocess

if __name__ == '__main__':

    trials = 50
    name = "yamaoka"

    #記録用CSVファイル作成
    f = open(name+"/alpha.csv", 'w')
    writer = csv.writer(f, lineterminator="\n")
    list = []

    for i in range(trials):

        alpha = random.randrange(20)
        cmd = "python sub.py "+str(name)+" "+str(alpha)
        pro = subprocess.Popen(cmd)

        while True:
            key = ord(getch())
            if key == 48: #上矢印
                print("↑")
                pro.terminate()#プロセス終了
                if alpha != 20:
                    alpha = alpha + 1#空気音に1近づける
                cmd = "python sub.py "+str(name)+" "+str(alpha)
                pro = subprocess.Popen(cmd)
            elif key == 55: #下矢印
                print("↓")
                pro.terminate()
                if alpha != 0:
                    alpha = alpha - 1#骨伝導音に1近づける
                cmd = "python sub.py "+str(name)+" "+str(alpha)
                pro = subprocess.Popen(cmd)
            elif key == 56:#ボタンを押されたら
                print("Enter")
                print("************Thank you*****************")
                print("")
                print("")
                print("***************Start******************")
                pro.terminate()
                list.append(alpha)
                ##print("alpha : " + str(alpha))
                break

    writer.writerow(list)
    print("実験終了 お疲れさまでした＾＾")
