class Tile:
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

class Circle:
    def __init__(self,x,y,c):
        self.x = x
        self.y = y
        self.c = c
    def display(self):
        fill(self.c)
        ellipse(self.x,self.y,50,50)

tiles = []
circles = []
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
        circles.append(Circle(random(25,width-25),random(25,75),qcolors[i]))

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
            r.display()
        else:
            r.display(color(200))

    for c in circles:
        c.display()

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

def mousePressed():
    for c in circles:
        d = dist(mouseX,mouseY,c.x,c.y)
        if d < 25:
            c.ox = mouseX
            c.oy = mouseY
            c.status = True
        else:
            c.status = False

def mouseDragged():
    for c in circles:
        if c.status and status==1:
            mx = mouseX - c.ox
            my = mouseY - c.oy
            c.x += mx
            c.y += my
            c.ox = mouseX
            c.oy = mouseY
