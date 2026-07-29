def setup():
    size(500,500)
    noStroke()

def draw():
    background(255)
    drawBall(width/2,height/2,200)

def drawBall(x, y, d):
    r = d / 2
    # 光源（左上）
    lightP = PVector(-1,-1)
    lightP.normalize()
    
    light = color(200)
    dark = color(0)
    for i in range(d,0,-1):
        t = 1 - i / float(d) # 0~1
        # 内側ほど光源方向へ少し移動
        offset = sin(t*HALF_PI) * r * 0.30
        cx = x + lightP.x * offset
        cy = y + lightP.y * offset

        c = lerpColor(light,dark,1-t)
        fill(c)
        ellipse(cx,cy,i,i)
