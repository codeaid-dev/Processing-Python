def setup():
    size(500,500)

def draw():
    background(255)
    if frameCount % 60 == 0:
        r=random(256)
        g=random(256)
        b=random(256)
        fill(r,g,b)
    ellipse(width/2,height/2,400,400)
