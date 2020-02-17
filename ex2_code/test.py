import sys
import wave
import pyaudio

def open(name):
    wf = wave.open(name+".wav", "r")
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

if __name__ == '__main__':
    number = 6
    name = "yamaoka"
    name = name + "/" + str(number)
    open(name)
