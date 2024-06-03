def setup():
    size(500,500)

def draw():
    background(255)
    stroke(0)
    noFill()
    drawCircle(width/2,height/2,width/2)

def drawCircle(x,y,radius):
    ellipse(x,y,radius,radius)
    if radius > 2:
        drawCircle(x+radius/2,y,radius/2)
        drawCircle(x-radius/2,y,radius/2)
