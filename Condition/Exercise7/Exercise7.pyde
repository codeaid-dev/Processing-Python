s = 20
cs = 3
def setup():
    size(500, 500)

def draw():
    global s, cs
    background(0)
    s += cs
    if s > width or s < 0:
        cs *= -1
    if s > 0 and s < width/3:
        fill(255,0,0)
    elif s > width/3 and s < width/3*2:
        fill(0,255,0)
    elif s > width/3*2 and width:
        fill(0,0,255)
    ellipse(width/2, height/2, s, s)
