x,y = 0,0 # マウスの座標
cx,cy = 250,250 # 楕円の中心座標
rw,rh = 100.0,200.0 # rw:楕円の横半径、rh:楕円の縦半径
def setup():
    size(500, 500)
    noStroke()
def draw():
    global x,y
    background(255)
    x = mouseX
    y = mouseY
    dx = x - cx
    dy = y - cy
    val = (dx*dx)/(rw*rw) + (dy*dy)/(rh*rh)
    if val <= 1:
        fill(255, 0, 0)
    else:
        fill(0)
    ellipse(cx, cy, rw*2, rh*2)
