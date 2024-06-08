class Circle:
    pass

circles = []

def setup():
    global x, y, dx, dy
    size(500, 500)
    for i in range(4):
        c = Circle()
        c.x = random(1,500)
        c.y = random(1,500)
        c.dx = random(2,4)
        c.dy = random(2,4)
        c.status = 0
        circles.append(c)

def draw():
    background(0)
    for c in circles:
        if c.status == 0:
            c.x += c.dx
            c.y += c.dy
            if c.x > width-20 or c.x < 20:
                c.dx *= -1
            if c.y > height-20 or c.y < 20:
                c.dy *= -1
        ellipse(c.x, c.y, 40, 40)

def mousePressed():
    for c in circles:
        dst = dist(mouseX, mouseY, c.x, c.y)
        if dst < 20:
            if c.status == 0:
                c.status = 1
            else:
                c.status = 0
