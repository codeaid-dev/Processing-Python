x, y = 250, 250
dx, dy = 3, 2

def setup():
    size(500, 500)

def draw():
    global x, y, dx, dy
    background(0)
    x += dx
    y += dy
    if x+75 > width or x-15 < 0:
        dx *= -1
    if y+15 > height or y-15 < 0:
        dy *= -1

    for i in range(3):
        ellipse(i*30+x, y, 30, 30)
