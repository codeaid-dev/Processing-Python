def setup():
    size(255,255)

def draw():
    background(255)
    w = width
    while w>0:
        fill(w)
        ellipse(width/2,height/2,w,w)
        w -= 25
