rw = 100 # 横の半径
rh = 200 # 縦の半径
def setup():
    size(500,500)
    noStroke()

def draw():
    background(255)
    fill(0)
    for i in range(0,360,10):
        rad = radians(i)
        x = width/2 + rw * cos(rad)
        y = height/2 + rh * sin(rad)
        ellipse(x,y,5,5)
