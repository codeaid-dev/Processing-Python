x,y,s = 300,200,30
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
        if keyCode == UP and dy == 0:
            dy = -12
        if keyCode == DOWN:
            dy += 2
        if keyCode == LEFT:
            dx -= 0.3
        if keyCode == RIGHT:
            dx += 0.3

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
