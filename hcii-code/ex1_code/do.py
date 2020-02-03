from open import openWave
from synthesis import synthesis
import sys

name = "yamaoka"

#ごちゃごちゃやるよう
if __name__ == '__main__':
    for i in range (21):
        synthesis(i/20,name)
