def setup():
    size(500, 500)

def draw():
    background(255)
    for i in range(26):
        line(i*20, 250, mouseX, mouseY)
