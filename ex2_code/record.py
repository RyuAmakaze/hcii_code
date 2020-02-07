#for graduation papper
import pyaudio
import sys
import time
import wave
import numpy

#WAVファイル作成, 引数は（ファイル名, 録音する秒数）
def MakeWavFile(FileName,Record_Seconds):
   chunk = 1024
   FORMAT = pyaudio.paInt16

   CHANNELS = 1 #モノラル
   RATE = 44100 #サンプルレート（録音の音質）

   p = pyaudio.PyAudio()

   stream = p.open(format = FORMAT,
                   channels = CHANNELS,
                   rate = RATE,
                   input = True,
                   frames_per_buffer = chunk)

   #レコード開始
   print("Now Recording...")
   all = []
   for i in range(0, int(RATE / chunk * Record_Seconds)):
       data = stream.read(chunk) #音声を読み取って、
       all.append(data) #データを追加

   #レコード終了
   print("Finished Recording.")

   stream.close()
   p.terminate()
   wavFile = wave.open(FileName, 'wb')
   wavFile.setnchannels(CHANNELS)
   wavFile.setsampwidth(p.get_sample_size(FORMAT))
   wavFile.setframerate(RATE)
   wavFile.writeframes(b"".join(all)) #Python3用

   wavFile.close()
