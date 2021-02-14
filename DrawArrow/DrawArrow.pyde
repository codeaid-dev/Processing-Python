def setup():
    size(600, 400)

def draw():
    background(0)
    drawArrow(x)

def drawArrow():
    fill(255)
    noStroke()
    rect(280, 190, 40, 20)
    triangle(250, 200, 280, 180, 280, 220)
    triangle(350, 200, 320, 180, 320, 220)
