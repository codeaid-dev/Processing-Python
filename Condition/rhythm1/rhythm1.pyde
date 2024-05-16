x,y = -5,160

def setup():
    size(1000,200)
    noStroke()

def draw():
    global x
    fill(0,10)
    rect(0,0,width,height)
    x += 2
    if x > width+5:
        x = -5
    fill(0,255,0)
    ellipse(x,y,10,10)
