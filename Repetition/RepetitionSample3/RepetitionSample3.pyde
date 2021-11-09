def setup():
    size(500, 500)

def draw():
    w, h = 10, 10
    background(0)
    for y in range(30):
        for x in range(30):
            rect(x*w+100, y*h+100, w, h)
