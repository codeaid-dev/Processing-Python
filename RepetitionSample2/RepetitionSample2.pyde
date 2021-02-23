def setup():
    size(500, 500)

def draw():
    w, h = 10, 10
    background(0)
    for y in range(30):
        for x in range(30):
            r = int(random(2))
            if r == 1:
                fill(255, 0, 0)
            else:
                fill(255)
            rect(x * w + 100, y * h + 100, w, h)
