move = 1
x = 100

def setup():
    size(600, 400)

def draw():
    global move, x
    if x > width-55:
        move = -1
    if x < 55:
        move = 1
    x += move
    background(0)
    drawArrow(x, 200)

def drawArrow(x, y):
    strokeWeight(20)
    stroke(255)
    line(x-25, y, x+25, y)
    fill(255)
    noStroke()
    triangle(x+55, y, x+25, y-20, x+25, y+20)
    triangle(x-55, y, x-25, y-20, x-25, y+20)
