r, g, b = 0, 0, 0

def setup():
    global r, g, b
    size(700, 700)
    r = random(256)
    g = random(256)
    b = random(256)

def draw():
    background(255)
    noStroke()
    for i in range(100):
        fill(r, g, b)
        x = 55 + 60 * (i % 10)
        y = 55 + 60 * (i / 10)
        rect(x, y, 50, 50)
