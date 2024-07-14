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
    x = width/2 + radius * cos(radians(angle))
    y = height/2 + radius * sin(radians(angle))
    fill(0)
    ellipse(x,y,10,10)
