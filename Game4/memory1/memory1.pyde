class Rect:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
    def display(self,c=None):
        if c==None:
            fill(self.c)
        else:
            fill(c)
        rect(self.x,self.y,100,100)

rects = []
colors = [color(255,0,0),
          color(0,255,0),
          color(0,0,255),
          color(255,255,0),
          color(0,255,255),
          color(255,0,255)]
qcolors = []

def setup():
    size(600,400)
    while True:
        num = int(random(6))
        if not colors[num] in qcolors:
            qcolors.append(colors[num])
        if len(qcolors) == 6:
            break
    for i in range(6):
        rects.append(Rect(50+i%3*200,100+i/3*150,qcolors[i]))

def draw():
    background(255)
    for r in rects:
        r.display()

    textAlign(CENTER)
    textSize(30)
    fill(255,0,0)
    text('Memory all',width/2,80)
