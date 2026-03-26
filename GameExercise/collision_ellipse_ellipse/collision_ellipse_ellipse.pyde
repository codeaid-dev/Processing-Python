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
    e2 = Ellipse()
    e2.cx = width/2
    e2.cy = height/2
    e2.rw = 50.0
    e2.rh = 100.0

def draw():
    background(255)
    e1.cx = mouseX
    e1.cy = mouseY
    fill(0,255,0)
    ellipse(e1.cx, e1.cy, e1.rw*2, e1.rh*2)
    if collision(e1, e2):
        fill(255, 0, 0, 150)
    else:
        fill(0)
    ellipse(e2.cx, e2.cy, e2.rw*2, e2.rh*2)

def collision(e1, e2):
    hit = False

    for i in range(0, 360, 5):
        t = radians(i)
        
        # e1の境界点
        ex = e1.cx + e1.rw * cos(t)
        ey = e1.cy + e1.rh * sin(t)

        # e2中心までの距離
        dx = ex - e2.cx
        dy = ey - e2.cy
        dist2 = dx*dx + dy*dy

        # e2の中に入っているかチェック
        if (dx*dx)/(e2.rw*e2.rw) + (dy*dy)/(e2.rh*e2.rh) <= 1:
            hit = True
            break

    return hit
