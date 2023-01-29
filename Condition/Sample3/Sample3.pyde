x = 50
move = 50

def setup():
    size(600, 200)

def draw():
    background(255)
    fill(0)
    ellipse(x, 100, 100, 100)

def mousePressed():
    global x
    if mouseButton == LEFT:
        x -= move
        if x < 50:
            x = width - 50
    if mouseButton == RIGHT:
        x += move
        if x > width - 50:
            x = 50
