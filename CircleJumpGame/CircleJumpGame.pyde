x, y, g = 0, 0, 0
w, h = 30, 30
sx, sy = 0, 0
gameOver = False
clear = False
count = 400

def setup():
    global x, y, g, w, h
    size(600, 400)
    x = 40
    y = 40
    g = 1
    w = 30
    h = 30

def draw():
    global x, y, w, h, sx, sy, g, gameOver, clear, count
    background(255)

    stroke(0)
    strokeWeight(6)
    line(10, 350, 60, 350)
    line(110, 300, 160, 300)
    line(210, 250, 260, 250)
    line(310, 200, 360, 200)
    line(410, 150, 460, 150)
    stroke(255, 0, 0)
    line(510, 100, 560, 100)

    noStroke()
    fill(0)
    ellipse(x, y, w, h)

    if gameOver:
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER", 300, 200)
        return

    if clear:
        textSize(50)
        textAlign(CENTER)
        text("CLEAR", 300, 200)
        return

    if x >= 10 and x <= 60 and y >= 347-w/2 \
        or x >= 110 and x <= 160 and y >= 293-w/2 \
        or x >= 210 and x <= 260 and y >= 247-w/2 \
        or x >= 310 and x <= 360 and y >= 193-w/2 \
        or x >= 410 and x <= 460 and y >= 147-w/2:
        g = 0
    elif x >= 510 and x <= 560 and y >= 93-w/2:
        g = 0
        clear = True
    else:
        g += 0.1

    if keyPressed:
        if keyCode == UP:
            sy -= 0.1
        if keyCode == DOWN:
            sy += 0.1
        if keyCode == LEFT:
            sx -= 0.1
        if keyCode == RIGHT:
            sx += 0.1
        if keyCode == 0:
            g = -3;

    sx *= 0.98
    sy *= 0.98
    x += sx
    y += sy
    y += g

    if x < w/2 or x > (width - w/2) or y < h/2 or y > (height - h/2):
        gameOver = True
