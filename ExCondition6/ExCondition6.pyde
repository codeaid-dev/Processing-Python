s = 20
cs = 3
def setup():
    size(300, 300)

def draw():
    global s, cs
    background(0)
    s += cs
    if s > width or s < 0:
        cs *= -1
    ellipse(width/2, height/2, s, s)
