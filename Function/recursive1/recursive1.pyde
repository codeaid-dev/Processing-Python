def setup():
    size(500,500)

def draw():
    background(255)
    stroke(0)
    noFill()
    drawCircle(width/2,height/2,width)

def drawCircle(x,y,radius):
    ellipse(x,y,radius,radius)
    if radius > 2:
        radius *= 0.75
        drawCircle(x,y,radius)
