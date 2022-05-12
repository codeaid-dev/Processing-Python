x, y = 250, 250
dx, dy = 2, 3

def setup():
    size(500, 500)

def draw():
    global x, y, dx, dy
    background(0)
    x += dx
    y += dy
    if x+25 > width or x-25 < 0:
        dx *= -1
    if y+25 > height or y-25 < 0:
        dy *= -1

    if x<width/2 and y<height/2:
        fill(255,0,0)
    elif x>width/2 and y<height/2:
        fill(0,255,0)
    elif x<width/2 and y>height/2:
        fill(255,255,0)
    elif x>width/2 and y>height/2:
        fill(0,0,255)

    ellipse(x, y, 50, 50)
