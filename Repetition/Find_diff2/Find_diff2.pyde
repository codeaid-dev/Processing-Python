def setup():
    size(700, 700)

def draw():
    background(255)
    noStroke()
    rectMode(CENTER)
    for i in range(100):
        fill(0)
        x = 80 + 60 * (i % 10)
        y = 80 + 60 * (i / 10)
        rect(x, y, 50, 50)
