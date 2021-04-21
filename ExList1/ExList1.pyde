x, y = [], []
dx, dy = [], []

def setup():
    global x, y, dx, dy
    size(500, 500)
    for i in range(3):
        x.append(250)
        y.append(250)
        dx.append(random(1,4))
        dy.append(random(1,4))

def draw():
    global x, y, dx, dy
    background(0)
    for i in range(3):
        x[i] += dx[i]
        y[i] += dy[i]
        if x[i] > width or x[i] < 0:
            dx[i] *= -1
        if y[i] > height or y[i] < 0:
            dy[i] *= -1
        ellipse(x[i], y[i], 30, 30)
