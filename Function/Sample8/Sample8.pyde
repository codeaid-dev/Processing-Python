def setup():
    size(600, 400)

def draw():
    background(0)
    drawArrow(125, 200)

def drawArrow(x, y):
    strokeWeight(20)
    stroke(255)
    line(x-25, y, x+25, y)
    fill(255)
    noStroke()
    triangle(x+55, y, x+25, y-20, x+25, y+20)
    triangle(x-55, y, x-25, y-20, x-25, y+20)
