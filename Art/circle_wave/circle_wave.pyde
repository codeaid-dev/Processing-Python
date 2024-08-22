x, y = 0, 0
dx = 1

def setup():
    size(500, 500)

def draw():
    global x, y, dx
    fill(0, 10)
    noStroke()
    rect(0, 0, width, height)
    fill(255)
    ellipse(x, y+height/2, 50, 50)
    if x < 0:
        dx += 1
    elif x > width:
        dx -= 1
    x += dx
    y = 100 * sin(radians(x))
