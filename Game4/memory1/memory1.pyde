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

def setup():
    size(600,400)
    for i in range(6):
        n = int(random(6))
        temp = colors[i]
        colors[i] = colors[n]
        colors[n] = temp
    for i in range(6):
        tiles.append(Tile(50+i%3*200,100+i/3*150,colors[i]))

def draw():
    background(255)
    for t in tiles:
        t.draw()

    textAlign(CENTER)
    textSize(30)
    fill(255,0,0)
    text('Memory all',width/2,80)
