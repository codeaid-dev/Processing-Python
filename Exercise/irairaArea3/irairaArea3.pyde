class Circle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s

    def display(self,c):
        fill(c)
        ellipse(self.x,self.y,self.s,self.s)

player = None
walls = []
def setup():
    global player,walls
    size(600,400)
    player = Circle(60,60,30)
    for i in range(54):
        x = i%9
        y = i/9
        c = color(255,0,0)
        w = Circle(x*66+34,y*66+34,30)
        walls.append(w)

def draw():
    background(255)
    noStroke()
    for w in walls:
        w.display(color(255,0,0))
    player.display(color(0))
    player.x = mouseX
    player.y = mouseY
