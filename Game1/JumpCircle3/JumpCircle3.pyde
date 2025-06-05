x,y,s = 300,200,30
up, down, left, right = False,False,False,False
dx,dy = 0,0
hx,hy,hs = [],[],[]
hc = 5
status = []

def setup():
    size(600,400)
    for i in range(hc):
        hx.append(random(width,width*2))
        ws = random(20,height/4)
        hs.append(ws)
        hy.append(height-ws/2)
        status.append(0)

def draw():
    global x,y,dx,dy
    background(255)
    noStroke()
    fill(0,0,255)
    ellipse(x,y,s,s)

    if y > height-s/2:
        dy = 0
        y = height-s/2
    else:
        dy += 0.3

    if keyPressed:
        if up and dy == 0:
            dy = -12
        if down:
            dy += 2
        if left:
            dx -= 0.1
        if right:
            dx += 0.1

    dx *= 0.98
    x += dx
    y += dy

    for i in range(hc):
        hx[i] -= 3
        if hx[i] < 0-hs[i]/2:
            hx[i] = random(width,width*2)
        hit()
        if status[i] == 0:
            fill(0)
        else:
            fill(255,0,0)
        ellipse(hx[i],hy[i],hs[i],hs[i])

def hit():
    global status
    for i in range(hc):
        dst = dist(x,y,hx[i],hy[i])
        if dst < (s+hs[i])/2:
            status[i] = 1

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
