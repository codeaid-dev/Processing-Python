def setup():
    size(300,300)

def draw():
    background(255)
    noStroke()
    y = 0
    while y*30 < height:
        x = 0
        while x*30 < width:
            fill(random(255))
            rect(x*30, y*30, 30, 30)
            x += 1
        y += 1
