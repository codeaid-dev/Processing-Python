dir=0
rw, rh = 200, 50 # rw:横半径、rh:縦半径
def setup():
    size(500,500)

def draw():
    global dir
    background(0)
    noStroke()
    fill(255,150,0)
    arc(width/2,height/2,200,200,radians(0),radians(180))
    x = width/2 + rw * cos(dir*PI/180)
    y = height/2 + rh * sin(dir*PI/180)
    fill(0,200,200)
    ellipse(x,y,20,20)
    fill(255,150,0)
    arc(width/2,height/2,200,200,radians(180),radians(360))
    dir+=0.5
