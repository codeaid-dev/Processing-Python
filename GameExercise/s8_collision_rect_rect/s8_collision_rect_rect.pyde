# 四角形1のx,y座標、幅、高さ
AX,AY,AW,AH = 100,100,100,100
# 四角形2のx,y座標、幅、高さ
BX,BY,BW,BH = 150,150,100,100

def setup():
  size(400, 400)

def draw():
    background(255)
    noStroke()

    AX = mouseX-50
    AY = mouseY-50
    fill(0,255,0)
    rect(AX, AY, AW, AH)
    
    if AX <= BX+BW and \
        AX+AW >= BX and \
        AY <= BY+BH and \
        AY+AH >= BY:
        fill(255,0,0,150)
    else:
        fill(0)
    rect(BX, BY, BW, BH)
