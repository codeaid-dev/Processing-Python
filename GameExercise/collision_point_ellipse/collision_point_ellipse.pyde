x,y = 0,0 # マウスの座標
cx,cy = 250,250 # 楕円の中心座標
rx,ry = 100.0,200.0 # rx:楕円の横半径、ry:楕円の縦半径
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
    val = (dx*dx)/(rx*rx) + (dy*dy)/(ry*ry)
    print(val)
    if val <= 1:
        fill(255, 0, 0)
    else:
        fill(0)
    ellipse(cx, cy, rx*2, ry*2)
