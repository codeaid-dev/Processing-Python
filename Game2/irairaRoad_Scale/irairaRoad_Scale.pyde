x, y = 0, 0
w, h = 30, 30
sx, sy = 0, 0
gameOver = False
clear = False
scale = 1.5
count = 400*scale
up, down, left, right = False,False,False,False

def setup():
    global x, y, w, h
    size(int(600*scale), int(400*scale))
    #size(600*scale, 400*scale)
    x = 60*scale
    y = 60*scale
    w = 30*scale
    h = 30*scale

def draw():
    global x, y, w, h, sx, sy, gameOver, clear, count
    background(255)
    noStroke()

    fill(255, 183, 0)
    rect(0, 0, 30*scale, count)
    count -= 0.1*scale

    fill("#FF0000")
    rect(125*scale, 0, 200*scale, 100*scale)
    rect(325*scale, 0, 150*scale, 250*scale)
    rect(125*scale, 150*scale, 150*scale, 250*scale)
    rect(275*scale, 300*scale, 200*scale, 100*scale)

    fill("#0000FF")
    rect(515*scale, 50*scale, 50*scale, 50*scale)

    if mousePressed and not gameOver:
        x = mouseX
        y = mouseY
    fill(0)
    ellipse(x, y, w, h)

    if gameOver:
        textSize(50*scale)
        textAlign(CENTER)
        text("GAME OVER", 300*scale, 200*scale)
        return

    if clear:
        textSize(50*scale)
        textAlign(CENTER)
        text("CLEAR", 300*scale, 200*scale)
        return

    if keyPressed:
        if up:
            sy -= 0.1
        if down:
            sy += 0.1
        if left:
            sx -= 0.1
        if right:
            sx += 0.1

    sx *= 0.98
    sy *= 0.98
    x += sx
    y += sy

    if x < w/2 or x > (width - w/2) or y < h/2 or y > (height - h/2):
        gameOver = True

    if (x >= 125*scale-w/2 and x <= 475*scale+w/2 and y <= 100*scale+h/2) \
        or (x >= 325*scale-w/2 and x <= 475*scale+w/2 and  y <= 250*scale+h/2) \
        or (x >= 125*scale-w/2 and x <= 475*scale+w/2 and y >= 300*scale-h/2) \
        or (x >= 125*scale-w/2 and x <= 275*scale+w/2 and y >= 150*scale-h/2) \
        or count < 0:
        gameOver = True

    if x >= 515*scale+w/2 and x <= 565*scale-w/2 and y >= 50*scale+w/2 and y <= 100*scale-w/2:
      clear = True

def keyPressed():
    global up, down, left, right
    if keyCode == UP:
        up = True
    if keyCode == DOWN:
        down = True
    if keyCode == LEFT:
        left = True
    if keyCode == RIGHT:
        right = True

def keyReleased():
    global up, down, left, right
    if keyCode == UP:
        up = False
    if keyCode == DOWN:
        down = False
    if keyCode == LEFT:
        left = False
    if keyCode == RIGHT:
        right = False
