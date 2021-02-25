def setup():
    size(300, 300)

def draw():
    cs = 30
    spaceX = (width-cs*5)/6
    spaceY = (height-cs*5)/6
    background(255)
    fill(0)
    for x in range(5):
        for y in range(5):
            ellipse(x*(spaceX+cs)+spaceX+cs/2, y*(spaceY+cs)+spaceY+cs/2, cs, cs)
