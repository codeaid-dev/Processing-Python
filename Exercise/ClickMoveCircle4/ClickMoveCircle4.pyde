x, y = [], []
dx, dy = [], []
status = []
def setup():
    global x, y, dx, dy
    size(500, 500)
    for i in range(4):
        x.append(random(1, 500))
        y.append(random(1, 500))
        dx.append(random(2, 4))
        dy.append(random(2, 4))
        status.append(0)

def draw():
    global x, y, dx, dy
    background(0)
    for i in range(4):
        if status[i] == 0:
            x[i] += dx[i]
            y[i] += dy[i]
            if x[i] > width-20 or x[i] < 20:
                dx[i] *= -1
            if y[i] > height-20 or y[i] < 20:
                dy[i] *= -1
        ellipse(x[i], y[i], 40, 40)

def mousePressed():
    global x, y
    for i in range(4):
        dst = dist(mouseX, mouseY, x[i], y[i])
        if dst < 20:
            if status[i] == 0:
                status[i] = 1
            else:
                status[i] = 0
