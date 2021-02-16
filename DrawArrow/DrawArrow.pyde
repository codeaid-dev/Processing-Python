def setup():
    size(600, 400)

def draw():
    background(0)
    drawArrow()

def drawArrow():
    fill(255)
    noStroke()
    rect(100, 190, 50, 20)
    triangle(180, 200, 150, 180, 150, 220)
