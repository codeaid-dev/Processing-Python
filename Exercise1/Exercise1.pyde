px, py, ps = 0, 0, 0
sx, sy = 0, 0

def setup():
    global px, py, ps
    size(600, 400)
    px = width/2
    py = height/2
    ps = 30

def draw():
    global px, py, ps, sx, sy
    background(255)
    fill(0)
    ellipse(px, py, ps, ps)

    if keyPressed:
        if keyCode == UP:
            sy -= 1
        if keyCode == DOWN:
            sy += 1
        if keyCode == LEFT:
            sx -= 1
        if keyCode == RIGHT:
            sx += 1

    sx *= 0.98
    sy *= 0.98
    px += sx
    py += sy
