radius = 0
angle = 0
def setup():
    global radius
    size(500,500)
    background(0)
    noStroke()
    radius = width/4

def draw():
    global angle
    angle += 0.1
    x = width/2 + radius * cos(radians(angle))
    y = height/2 + radius * sin(radians(angle))
    fill(255)
    ellipse(x,y,5,5)
    ex = x + radius * cos(radians(angle)*36)
    ey = y + radius * sin(radians(angle)*36)
    fill(255,0,0)
    ellipse(ex,ey,5,5)
