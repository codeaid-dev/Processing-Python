x,y = 300,300

def setup():
    size(600,600)
    noStroke()

def draw():
    background(0)
    fill(255,255,0)
    arc(x,y,30,30,radians(45),radians(315))
