x, y = 0, 0
w, h = 30, 30
sx, sy = 0, 0
gameOver = False
clear = False
count = 400

def setup():
    global x, y, w, h
    size(600, 400)
    x = 60
    y = 60
    w = 30
    h = 30

def draw():
    global x, y, w, h, sx, sy, gameOver, clear, count
    background(255)
    noStroke()

    fill(255, 183, 0)
    rect(0, 0, 30, count)
    count -= 0.1

    fill("#FF0000")
    rect(125, 0, 200, 100)
    rect(325, 0, 150, 250)
    rect(125, 150, 150, 250)
    rect(275, 300, 200, 100)

    fill("#0000FF")
    rect(515, 50, 50, 50)

    if mousePressed and not gameOver:
        x = mouseX
        y = mouseY
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

    if keyPressed:
        if keyCode == UP:
            sy -= 0.1
        if keyCode == DOWN:
            sy += 0.1
        if keyCode == LEFT:
            sx -= 0.1
        if keyCode == RIGHT:
            sx += 0.1

    sx *= 0.98
    sy *= 0.98
    x += sx
    y += sy

    if x < w/2 or x > (width - w/2) or y < h/2 or y > (height - h/2):
        gameOver = True

    if (x >= 125-w/2 and x <= 475+w/2 and y <= 100+h/2) \
        or (x >= 325-w/2 and x <= 475+w/2 and  y <= 250+h/2) \
        or (x >= 125-w/2 and x <= 475+w/2 and y >= 300-h/2) \
        or (x >= 125-w/2 and x <= 275+w/2 and y >= 150-h/2) \
        or count < 0:
        gameOver = True

    if x >= 515+w/2 and x <= 565-w/2 and y >= 50+w/2 and y <= 100-w/2:
      clear = True
