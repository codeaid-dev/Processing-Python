dir=0
radius=125
def setup():
    size(500,500)
    background(0)
    noStroke()

def draw():
    global dir
    x = width/2 + radius * cos(dir*PI/180)
    y = height/2 + radius * sin(dir*PI/180)
    fill(255)
    ellipse(x,y,5,5)
    mx = x + radius * cos((dir*PI/180)*36)
    my = y + radius * sin((dir*PI/180)*36)
    fill(255,0,0)
    ellipse(mx,my,5,5)
    dir+=0.1
