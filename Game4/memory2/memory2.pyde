class Tile:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
    def draw(self,c=None):
        if c==None:
            fill(self.c)
        else:
            fill(c)
        rect(self.x,self.y,100,100)

tiles = []
colors = [color(255,0,0),
          color(0,255,0),
          color(0,0,255),
          color(255,255,0),
          color(0,255,255),
          color(255,0,255)]
qcolors = []
saved_time = millis()
status = 0 # 0:memory, 1:doing, 2:show

def setup():
    size(600,400)
    while True:
        num = int(random(6))
        if not colors[num] in qcolors:
            qcolors.append(colors[num])
        if len(qcolors) == 6:
            break
    for i in range(6):
        tiles.append(Tile(50+i%3*200,100+i/3*150,qcolors[i]))

def draw():
    global saved_time,status
    background(255)
    if status == 0:
        timer = 5 - ((millis()-saved_time)/1000)
    elif status == 1:
        timer = 10 - ((millis()-saved_time)/1000)
    else:
        timer = 0
    if timer == 0 and status != 2:
        status += 1
        if status == 1:
            saved_time = millis()
    for r in tiles:
        if status == 0 or status == 2:
            r.draw()
        else:
            r.draw(color(200))

    textAlign(CENTER)
    textSize(30)
    fill(255,0,0)
    if status == 0:
        text('Memory all',width/2,80)
    elif status == 1:
        text('Put all circles on each tile',width/2,80)
    else:
        text('Done',width/2,80)
    text(timer,width/2,50)
