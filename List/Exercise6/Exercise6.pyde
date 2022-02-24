x, y = [], []
dx, dy = [], []

def setup():
    size(500, 500)
    for i in range(3):
        x.append(250)
        y.append(250)
        dx.append(random(1,4))
        dy.append(random(1,4))

def draw():
    background(0)
    for i in range(3):
        x[i] += dx[i]
        y[i] += dy[i]
        if x[i] > width-15 or x[i] < 15:
            dx[i] *= -1
        if y[i] > height-15 or y[i] < 15:
            dy[i] *= -1
        ellipse(x[i], y[i], 30, 30)
