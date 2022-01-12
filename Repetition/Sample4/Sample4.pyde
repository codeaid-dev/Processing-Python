def setup():
    size(300, 300)

def draw():
    w, h = 10, 10
    for y in range(30):
        for x in range(30):
            r = random(255)
            g = random(255)
            b = random(255)
            fill(r, g, b)
            rect(x * w, y * h, w, h)
