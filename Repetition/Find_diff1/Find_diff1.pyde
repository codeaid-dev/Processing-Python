def setup():
    size(700, 700)

def draw():
    background(255)
    noStroke()
    for i in range(10):
        for j in range(10):
            fill(0)
            x = 55 + 60 * i
            y = 55 + 60 * j
            rect(x, y, 50, 50)
