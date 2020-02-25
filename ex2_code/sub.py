import sys
import wave
import pyaudio
import time

#time.sleep(0.2)
t0 = time.time()

args = sys.argv

wf = wave.open(str(args[1])+"/"+str(args[2])+".wav", "r")
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# チャンク単位でストリームに出力し音声を再生
chunk = 1024
data = wf.readframes(chunk)
while data != b'':
    stream.write(data)
    data = wf.readframes(chunk)
stream.close()
p.terminate()

t1 = time.time()
print("再生時間："+str(t1-t0)+"[s]")
