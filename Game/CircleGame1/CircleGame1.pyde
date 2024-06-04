x, y  = 0, 0
w, h = 30, 30
sx, sy = 0, 0
gameOver = False
r1,r2 = False,False

def setup():
    global x, y, w, h
    size(600, 400)
    x = width/2
    y = height/2
    w = 30
    h = 30

def draw():
    global x, y, w, h, sx, sy, gameOver, r1, r2
    background(255)
    fill(255)
    if x+w/2 >= 50 and x-w/2 <= 50+100 \
        and y+h/2 >= 50 and y-h/2 <= 50+100:
        r1 = True
    if r1:
        fill(255,0,0)
    else:
        fill(255)
    rect(50, 50, 100, 100)

    if x+w/2 >= 450 and x-w/2 <= 450+100 \
        and y+h/2 >= 250 and y-h/2 <= 250+100:
        r2 = True
    if r2:
        fill(0,0,255)
    else:
        fill(255)
    rect(450, 250, 100, 100)

    fill(0)
    ellipse(x, y, w, h)

    if r1 and r2:
        textSize(50)
        textAlign(CENTER)
        text("CLEAR", 300, 200)
        return
        
    if gameOver:
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER", 300, 200)
        return

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
    x += sx
    y += sy

    if x < w/2 or x > (width - w/2) or y < h/2 or y > (height - h/2):
        gameOver = True
