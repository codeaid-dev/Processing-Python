def setup():
    size(500, 500)

def draw():
    background(255)
    x = [50, 100, 150, 200, 250, 300, 350, 400, 450]
    y = [50, 100, 150, 200, 250, 300, 350, 400, 450]
    for i in range(9):
        ellipse(x[i], y[i], 20, 20)
