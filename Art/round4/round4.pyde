angle=0
px,py = 0,0
radius = 200
def setup():
    global px,py
    size(500,500)
    px = width/2 + radius * cos(radians(angle))
    py = height/2 + radius * sin(radians(angle))
    strokeWeight(10)

def draw():
    global angle,px,py
    angle += 1
    x = width/2 + radius * cos(radians(angle))
    y = height/2 + radius * sin(radians(angle))
    stroke(0)
    line(px,py,x,y)
    px,py = x,y
