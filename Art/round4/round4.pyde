angle=0
radius = 200
def setup():
    size(500,500)
    fill(0)
    noStroke()

def draw():
    global angle
    angle += 1
    x = width/2 + radius * cos(radians(angle))
    y = height/2 + radius * sin(radians(angle))
    ellipse(x,y,10,10)
