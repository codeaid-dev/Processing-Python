def setup():
    size(500, 500)

def draw():
    background(0)
    drawHouse()

def drawHouse():
    fill(255, 0, 0)
    triangle(250, 100, 150, 200, 350, 200)
    fill(255)
    rect(180, 200, 140, 100)
    fill(255, 255, 0)
    ellipse(250, 250, 50, 50)
    line(250, 225, 250, 275)
    line(225, 250, 275, 250)
