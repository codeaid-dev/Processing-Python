x, y = 250, 250
dx, dy = 3, 2

def setup():
    size(500, 500)

def draw():
    global x, y, dx, dy
    background(0)
    x += dx
    y += dy
    if 60+x > width or x < 0:
        dx *= -1
    if y > height or y < 0:
        dy *= -1

    for i in range(3):
        ellipse(i*30+x, y, 30, 30)
