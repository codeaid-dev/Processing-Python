px,py = 0,0
psize = 20
def setup():
    size(600,400)

def draw():
    global px,py
    background(0)
    px = mouseX
    py = mouseY
    noStroke()
    fill(255)
    ellipse(px,py,psize,psize)
