def setup():
    size(300, 300)

def draw():
    w, h = 10, 10
    for y in range(30):
        for x in range(30):
            rect(x * w, y * h, w, h)
