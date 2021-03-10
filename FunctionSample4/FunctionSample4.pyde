move = 1
x = 100

def setup():
    size(600, 400)

def draw():
    global move, x
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
'''
    strokeWeight(20)
    stroke(255)
    line(100, 200, 150, 200)
    fill(255)
    noStroke()
    triangle(180, 200, 150, 180, 150, 220)
    triangle(70, 200, 100, 180, 100, 220)
'''
