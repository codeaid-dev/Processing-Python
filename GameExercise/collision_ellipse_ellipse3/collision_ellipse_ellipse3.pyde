class Ellipse:
    pass
e1,e2 = None,None
def setup():
    global e1,e2
    size(500, 500)
    noStroke()
    e1 = Ellipse()
    e1.cx = mouseX
    e1.cy = mouseY
    e1.rw = 100.0
    e1.rh = 50.0
    e1.angle = radians(45)
    e2 = Ellipse()
    e2.cx = width/2
    e2.cy = height/2
    e2.rw = 50.0
    e2.rh = 100.0
    e2.angle = radians(45)

def draw():
    background(255)
    e1.cx = mouseX
    e1.cy = mouseY
    fill(0,255,0)
    pushMatrix()
    translate(e1.cx, e1.cy)
    rotate(e1.angle)
    ellipse(0, 0, e1.rw*2, e1.rh*2)
    popMatrix()
    if collision(e1, e2):
        fill(255, 0, 0, 150)
    else:
        fill(0)
    pushMatrix()
    translate(e2.cx, e2.cy)
    rotate(e2.angle)
    ellipse(0, 0, e2.rw*2, e2.rh*2)
    popMatrix()

def collision(e1, e2):
    # e1 → e2 をチェック
    for i in range(0, 360, 5):
        t = radians(i)
        x, y = getPoint(e1, t)
        
        if isInEllipse(e2, x, y):
            return True

    # e2 → e1 もチェック
    for i in range(0, 360, 5):
        t = radians(i)
        x, y = getPoint(e2, t)
        
        if isInEllipse(e1, x, y):
            return True

    return False

def getPoint(e, rad):
    # 楕円（回転前）
    x = e.rw * cos(rad)
    y = e.rh * sin(rad)
    # 回転
    xr = x * cos(e.angle) - y * sin(e.angle)
    yr = x * sin(e.angle) + y * cos(e.angle)
    # 平行移動
    ex = e.cx + xr
    ey = e.cy + yr
    
    return ex, ey

def isInEllipse(e, x, y):
    # 楕円中心基準の点座標
    dx = x - e.cx
    dy = y - e.cy
    # 逆回転
    ca = cos(-e.angle)
    sa = sin(-e.angle)
    # 逆回転後の楕円中心基準の点座標
    nx = dx * ca - dy * sa
    ny = dx * sa + dy * ca
    # 通常の楕円当たり判定
    val = (nx*nx)/(e.rw*e.rw) + (ny*ny)/(e.rh*e.rh)
    return val <= 1.0
