x, y, g = 0, 0, 0
w, h = 30, 30
sx, sy = 0, 0
over = False
clear = False
count = 400
up, left, right = False,False,False

def setup():
    global x, y, g, w, h
    size(600, 400)
    x = 40
    y = 40
    g = 1
    w = 30
    h = 30

def draw():
    global x, y, w, h, sx, sy, g, over, clear, count
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

    if over:
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER", 300, 200)
        return

    if clear:
        textSize(50)
        textAlign(CENTER)
        text("CLEAR", 300, 200)
        return

    if 10 <= x <= 60 and 350 >= y >= 347-w/2 \
        or 110 <= x <= 160 and 300 >= y >= 293-h/2 \
        or 210 <= x <= 260 and 250 >= y >= 247-h/2 \
        or 310 <= x <= 360 and 200 >= y >= 193-h/2 \
        or 410 <= x <= 460 and 150 >= y >= 147-h/2:
        g = 0
    elif 510 <= x <= 560 and 100 >= y >= 93-h/2:
        g = 0
        clear = True
    else:
        g += 0.1

    if keyPressed:
        if up and g == 0:
            sy -= 7
        if left:
            sx -= 0.1
        if right:
            sx += 0.1

    sx *= 0.98
    sy *= 0.98
    x += sx
    y += sy
    y += g

    if x < w/2 or x > (width - w/2) or y < h/2 or y > (height - h/2):
        over = True

def keyPressed():
    global up, left, right
    if keyCode == UP:
        up = True
    if keyCode == LEFT:
        left = True
    if keyCode == RIGHT:
        right = True

def keyReleased():
    global up, left, right
    if keyCode == UP:
        up = False
    if keyCode == LEFT:
        left = False
    if keyCode == RIGHT:
        right = False
