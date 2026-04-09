dir=0
radius=200
def setup():
    size(500,500)

def draw():
    global dir
    background(0)
    noStroke()
    fill(255,150,0)
    ellipse(width/2,height/2,40,40)
    x = width/2 + radius * cos(dir*PI/180)
    y = height/2 + radius * sin(dir*PI/180)
    fill(0,200,200)
    ellipse(x,y,20,20)
    mx = x + 30 * cos(dir*12*PI/180)
    my = y + 30 * sin(dir*12*PI/180)
    fill(255)
    ellipse(mx,my,5,5)
    dir+=0.5
