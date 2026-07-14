class Circle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s
        self.goal = False

    def draw(self,c):
        fill(c)
        ellipse(self.x,self.y,self.s,self.s)

player = None
walls = []
def setup():
    global player
    size(600,400)
    player = Circle(67,15,30)
    goal = int(random(54))
    for i in range(54):
        x = i%9
        y = i/9
        c = color(255,0,0)
        w = Circle(x*66+34,y*66+34,30)
        if i == goal:
            w.goal = True
        walls.append(w)

def draw():
    background(255)
    noStroke()
    for w in walls:
        if w.goal:
            w.draw(color(0,0,255))
        else:
            w.draw(color(255,0,0))
    player.draw(color(0))

playing = False
def mouseMoved():
    global playing
    if not playing:
        if dist(mouseX,mouseY,player.x,player.y) <= 15:
            playing = True
        return
    if mouseX > player.s/2 and \
      mouseX < width-player.s/2 and \
      mouseY > player.s/2 and \
      mouseY < height-player.s/2:
        player.x = mouseX
        player.y = mouseY
