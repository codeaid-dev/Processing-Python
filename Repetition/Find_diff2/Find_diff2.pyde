def setup():
    size(700, 700)

def draw():
    background(255)
    noStroke()
    for i in range(100):
        fill(0)
        x = 55 + 60 * (i % 10)
        y = 55 + 60 * (i / 10)
        rect(x, y, 50, 50)
