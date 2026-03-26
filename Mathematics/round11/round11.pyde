rw = 100 # 横の半径
rh = 200 # 縦の半径
angle = radians(45) # 楕円の傾く角度
def setup():
    size(500,500)
    noStroke()

def draw():
    background(255)
    fill(0)

    cx = width/2
    cy = height/2

    for i in range(0,360,10):
        rad = radians(i)
        # 楕円（回転前）
        x = rw * cos(rad)
        y = rh * sin(rad)
        # 回転
        xr = x * cos(angle) - y * sin(angle)
        yr = x * sin(angle) + y * cos(angle)
        # 平行移動
        ex = cx + xr
        ey = cy + yr

        ellipse(ex, ey, 5, 5)
