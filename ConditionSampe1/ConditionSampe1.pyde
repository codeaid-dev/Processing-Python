x = 50
move = 1

def setup():
    size(600, 200)

def draw():
    global x, move
    background(255)
    fill(0)
    x += move
    if x >= width-50:
        move = -1
    if x-50 <= 0:
        move = 1
    ellipse(x, 100, 100, 100)
