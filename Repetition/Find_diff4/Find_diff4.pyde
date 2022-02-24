r, g, b = 0, 0, 0
a, atari = 0, 0

def setup():
    global r, g, b, a, atari
    size(700, 700)
    r = random(256)
    g = random(256)
    b = random(256)
    a = random(100, 250)
    atari = int(random(0, 100))

def draw():
    background(255)
    noStroke()
    for i in range(100):
        if i == atari:
            fill(r, g, b, a)
        else:
            fill(r, g, b)
        x = 55 + 60 * (i % 10)
        y = 55 + 60 * (i / 10)
        rect(x, y, 50, 50)
