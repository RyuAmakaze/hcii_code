from msvcrt import getch
##キーがordでどのように変換されているかをチェックする
## 7 →　55, 8 →　56, 9 → 57 ,
## Enter →　13


key = ord(getch())
print(key)
if(key==8):
    print("hello")
