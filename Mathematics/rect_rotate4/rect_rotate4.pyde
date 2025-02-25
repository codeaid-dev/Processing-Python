rects = []

class Rect:
    pass

def setup():
    size(500,500)
    for i in range(4):
        r = Rect()
        r.x = 125+i%2*250
        r.y = 125+i/2*250
        r.angle = 0
        r.speed = 1
        #r.rad = radians(r.angle)
        r.rad = radians(r.speed)
        rects.append(r)

def draw():
    background(0)
    fill(255)
    rectMode(CENTER)
    for r in rects:
        pushMatrix()
        translate(r.x,r.y)
        #r.angle += r.speed
        r.rad += radians(r.speed)
        rotate(r.rad)
        rect(0,0,50,50)
        popMatrix()
