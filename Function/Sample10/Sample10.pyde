s = 20
def setup():
    size(300, 300)

def draw():
    global s
    background(0)
    fill(255,0,0)
    ellipse(width/2, height/2, s, s)

def mouseClicked():
    global s
    s += 2
