x, y = 0, 0
dx, dy = 2, 3
def setup():
    global x, y
    size(500, 500)
    x = random(1, 500)
    y = random(1, 500)

def draw():
    global x, y, dx, dy
    background(0)
    x += dx
    y += dy
    if x > width or x < 0:
        dx *= -1
    if y > height or y < 0:
        dy *= -1
    ellipse(x, y, 40, 40)
