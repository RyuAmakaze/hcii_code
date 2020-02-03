import tkinter as tk
import random
#from png import show,show_str

# 点滅するボール
class Ball(object):
    root = None
    canvas = None

    # pos=位置, fill=色, dt=点滅間隔[msec]
    def __init__(self,id,pos,fill,dt):
        self.id= str(id)
        #self.state = 'normal'
        self.dt = dt
        Ball.canvas.create_oval( 100,100,100+50,100+50, tags=self.id, fill="red")
        Ball.root.after(self.dt, self.blink)

    def blink(self):
        #if self.state == 'normal':
        #    self.state = 'hidden'
        #else:
        #    self.state = 'normal'

        pos = 10*random.randrange(15)
        Ball.canvas.delete("1")
        print(pos)
        Ball.canvas.create_oval( pos,pos,pos+50,pos+50, tags=1, fill="red")
        Ball.canvas.delete("1")

        #self.canvas.itemconfigure(self.id, state=self.state)
        self.root.after(self.dt, self.blink)


class MyFrame(tk.Frame):

    def __init__(self,root):
        tk.Frame.__init__(self,root)
        self.root = root
        self.pack()

        self.canvas = tk.Canvas(self, width=300, height=300, bg="white")
        self.canvas.pack()

        Ball.root = root
        Ball.canvas = self.canvas

        self.b1 = Ball(1, 100, 'red', 400)
        #self.b2 = Ball(2, 100, 'blue', 500)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('count')
    frame = MyFrame(root)
    root.geometry('-2700+900')
    frame.mainloop()
