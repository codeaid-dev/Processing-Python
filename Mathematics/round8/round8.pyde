angle=0
radius = 200
def setup():
    size(500,500)
    noStroke()

def draw():
    global angle
    fill(255,10)
    rect(0,0,width,height)
    angle += 1
    x = width/2 + radius * cos(radians(angle*3))
    y = height/2 + radius * sin(radians(angle*4))
    fill(0)
    ellipse(angle,y,10,10)
    if angle>width: angle=0
