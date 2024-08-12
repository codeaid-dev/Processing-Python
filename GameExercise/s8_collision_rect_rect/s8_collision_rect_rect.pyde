# 四角形1のx,y座標、幅、高さ
rect1X,rect1Y,rect1W,rect1H = 100,100,100,100
# 四角形2のx,y座標、幅、高さ
rect2X,rect2Y,rect2W,rect2H = 150,150,100,100

def setup():
  size(400, 400)

def draw():
    background(255)
    noStroke()

    rect1X = mouseX-50
    rect1Y = mouseY-50
    fill(0,255,0)
    rect(rect1X, rect1Y, rect1W, rect1H)
    
    if rect1X < rect2X+rect2W and \
        rect1X+rect1W > rect2X and \
        rect1Y < rect2Y+rect2H and \
        rect1Y+rect1H > rect2Y:
        fill(255,0,0,150)
    else:
        fill(0)
    rect(rect2X, rect2Y, rect2W, rect2H)
