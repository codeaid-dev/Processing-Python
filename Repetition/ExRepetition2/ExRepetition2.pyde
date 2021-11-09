def setup():
    size(500, 500)

def draw():
    background(255)
    for x in range(26):
        for y in range(26):
            line(x*20, y*20, mouseX, mouseY)
