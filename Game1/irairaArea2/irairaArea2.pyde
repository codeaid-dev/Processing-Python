class Circle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s

    def draw(self,c):
        fill(c)
        ellipse(self.x,self.y,self.s,self.s)

player = None
def setup():
    global player
    size(600,400)
    player = Circle(67,15,30)

def draw():
    background(255)
    noStroke()
    player.draw(color(0))

def mouseMoved():
    if mouseX > player.s/2 and \
      mouseX < width-player.s/2 and \
      mouseY > player.s/2 and \
      mouseY < height-player.s/2:
        player.x = mouseX
        player.y = mouseY
