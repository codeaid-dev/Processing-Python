x, y = 0, 0
dx, dy = 2, 3
status = 0
def setup():
    global x, y
    size(500, 500)
    x = random(1, 500)
    y = random(1, 500)

def draw():
    global x, y, dx, dy, status
    background(0)
    if status == 0:
        x += dx
        y += dy
        if x > width-20 or x < 20:
            dx *= -1
        if y > height-20 or y < 20:
            dy *= -1
    ellipse(x, y, 40, 40)

def mousePressed():
    global status
    dst = dist(mouseX, mouseY, x, y)
    if dst < 20:
        status = 1 if status == 0 else 0
