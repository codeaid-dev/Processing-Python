def setup():
    size(500, 500)

def draw():
    background(0)
    drawHouse(150, 100)
    drawHouse(350, 100)

def drawHouse(x, y):
    fill(255, 0, 0)
    triangle(x, y, x-100, y+100, x+100, y+100)
    fill(255)
    rect(x-70, y+100, 140, 100)
    fill(255, 255, 0)
    ellipse(x, y+150, 50, 50)
    line(x, y+125, x, y+175)
    line(x-25, y+150, x+25, y+150)
