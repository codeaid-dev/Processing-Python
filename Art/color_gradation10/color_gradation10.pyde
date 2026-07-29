x,y,dx,dy = 0,0,0,0
r=25
light,dark = 0,0

def setup():
    global x,y,dx,dy,light,dark
    size(500,500)
    noStroke()
    x = width/2
    y = height/2
    angle = random(TWO_PI)
    speed = random(5,8)
    dx = speed*cos(angle)
    dy = speed*sin(angle)
    light = color(200)
    dark = color(0)

def draw():
    global x,y,dx,dy
    background(255)
    x += dx
    y += dy
    if x < r or x > width-r:
        dx *= -1
    if y < r or y > height-r:
        dy *= -1
    drawBall(x,y,r*2)

def drawBall(x, y, d):
    r = d / 2
    # 光源（左上）
    lightP = PVector(-1,-1)
    lightP.normalize()

    for i in range(d,0,-1):
        t = 1 - i / float(d) # 0~1
        # 内側ほど光源方向へ少し移動
        offset = sin(t*HALF_PI) * r * 0.30
        cx = x + lightP.x * offset
        cy = y + lightP.y * offset

        c = lerpColor(light,dark,1-t)
        fill(c)
        ellipse(cx,cy,i,i)

def mousePressed():
    global x,y,dx,dy,light,dark
    x = mouseX
    y = mouseY
    angle = random(TWO_PI)
    speed = random(3,6)
    dx = speed*cos(angle)
    dy = speed*sin(angle)
    r = random(256)
    g = random(256)
    b = random(256)
    light = color(r+50,g+50,b+50)
    dark = color(r,g,b)
