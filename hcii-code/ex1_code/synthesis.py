import wave
import struct
import numpy as np
from pylab import *

#Boneへの重みαを変更して合成
#チャンネルの数は1じゃないとできない
def save(data, fs, bit, filename):
    """波形データをWAVEファイルへ出力"""
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(bit // 8)
    wf.setframerate(fs)
    wf.writeframes(data)
    wf.close()

def printWaveInfo(wf):
    """WAVEファイルの情報を取得"""
    print("チャンネル数:", wf.getnchannels())
    print("サンプル幅:", wf.getsampwidth())
    print("サンプリング周波数:", wf.getframerate())
    print("フレーム数:", wf.getnframes())
    print("パラメータ:", wf.getparams())
    print("長さ（秒）:", float(wf.getnframes()) / wf.getframerate())

#波形合成して保存,output : synthesis_alpha
def synthesis(alpha,name):

    wf1 = wave.open(name+"/air.wav", "r")
    fs1 = wf1.getnframes() #総フレーム数
    samf1 = wf1.getframerate() #サンプリング周波数
    wf2 = wave.open(name+"/bone.wav", "r")
    fs2 = wf2.getnframes() #総フレーム数
    samf2 = wf2.getframerate() #サンプリング周波数

    #音源情報提示
    #printWaveInfo(wf1)
    #printWaveInfo(wf2)

    #ファイルを開いてから、量子化ビット16なので、32768で各フレームの値を-1~1で正規化
    x = wf1.readframes(fs1)
    x = frombuffer(x, dtype="int16") / 32768.0
    y = wf2.readframes(fs2)
    y = frombuffer(y, dtype="int16") / 32768.0

    #波形合成
    if(fs1>=fs2):
        z = [0.0]*(fs2)
        for n in range(fs2):
            z[n] = alpha*x[n] + (1-alpha)*y[n]
    else:
        z = [0.0]*(fs1)
        for n in range(fs1):
            z[n] = alpha*x[n] + (1-alpha)*y[n]


    #for i in range(80300):
    #    print("z:" + str(z[i]))
    #    print("x:" + str(x[i]))
    #    print("y:" + str(y[i]))

    z = [int(k* 32767.0) for k in z]
    z = struct.pack("h" * len(z), *z)
    save(z, samf1, 16,name+"/synthesis_"+str(int(alpha*20))+".wav")
    print(name+"/synthesis_"+str(int(alpha*20))+".wav")
