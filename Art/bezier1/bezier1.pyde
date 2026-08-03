def setup():
    size(500,500)

def draw():
    background(255)
    leftX = 50
    topY = 50
    rightX = 450
    bottomY = 450
    pitch = (rightX-leftX)/50 # 線幅
    distortion = 400 # 上下の歪み
    stroke(200,0,0)
    noFill()
    for i in range(50):
        x = leftX+i*pitch
        y = bottomY-i*pitch
        bezier(leftX,topY,
            x,y+distortion,
            x,y-distortion,
            rightX,bottomY)
