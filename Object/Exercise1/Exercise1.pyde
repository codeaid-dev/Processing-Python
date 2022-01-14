class Circle:
    def __init__(self,x,y,s,iro):
        self.x = x
        self.y = y
        self.s = s
        self.iro = iro

ens = []
count = 0

def setup():
    size(600, 400)

def draw():
    background(0)
    for p in ens:
        p.x += 1
        noStroke()
        fill(p.iro)
        ellipse(p.x,p.y,p.s,p.s)

def mousePressed():
    global ens,count
    if count < 50:
        iro = color(random(256),random(256),random(256))
        en = Circle(0,random(height),random(10,30),iro)
        ens.append(en)
        count += 1
