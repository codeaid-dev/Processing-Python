def setup():
    size(600, 400)
    noStroke()

def draw():
    for i in range(20):
        fill(i*12, mouseX/3, 255)
        rect(30*i, 0, 30, 400)
