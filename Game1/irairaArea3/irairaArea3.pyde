class Circle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s

    def draw(self,c):
        fill(c)
        ellipse(self.x,self.y,self.s,self.s)

player = None
walls = []
def setup():
    global player
    size(600,400)
    player = Circle(67,15,30)
    for i in range(54):
        x = i%9
        y = i/9
        w = Circle(x*66+34,y*66+34,30)
        walls.append(w)

def draw():
    background(255)
    noStroke()
    for w in walls:
        w.draw(color(255,0,0))
    player.draw(color(0))

def mouseMoved():
    if mouseX > player.s/2 and \
      mouseX < width-player.s/2 and \
      mouseY > player.s/2 and \
      mouseY < height-player.s/2:
        player.x = mouseX
        player.y = mouseY
