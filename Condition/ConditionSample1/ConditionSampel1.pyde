x = 50

def setup():
    size(600, 200)

def draw():
    global x
    background(255)
    fill(0)
    x += 1
    if x >= width-50:
        x = width-50
    ellipse(x, 100, 100, 100)
