x,y = 0,0 # マウスの座標
cx,cy = 250,250 # 楕円の中心座標
rw,rh = 100.0,200.0 # rw:楕円の横半径、rh:楕円の縦半径
angle = radians(45) # 楕円の傾き(ラジアン値)
def setup():
    size(500, 500)
    noStroke()
def draw():
    global x,y
    background(255)
    x = mouseX
    y = mouseY
    if collision():
        fill(255, 0, 0)
    else:
        fill(0)
    pushMatrix()
    translate(cx, cy)
    rotate(angle)
    ellipse(0, 0, rw*2, rh*2)
    popMatrix()

def collision():
    # 楕円中心基準の点座標
    dx = x - cx
    dy = y - cy
    # 逆回転
    ca = cos(-angle)
    sa = sin(-angle)
    # 逆回転後の楕円中心基準の点座標
    nx = dx * ca - dy * sa
    ny = dx * sa + dy * ca
    # 通常の楕円当たり判定
    val = (nx*nx)/(rw*rw) + (ny*ny)/(rh*rh)
    return val <= 1.0
