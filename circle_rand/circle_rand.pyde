def setup():
    size(600, 600)
    background(0)
    noStroke()

def draw():
    x = random(0, width)
    y = random(0, height)
    dst = dist(x, y, width/2, height/2)
    diameter = (height/2 - dst) / 10
    if diameter > 0:
        fill(0,0,255)
        ellipse(x, y, diameter, diameter)
