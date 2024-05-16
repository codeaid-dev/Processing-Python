x,y = -5,160
dy = 5
flag = False

def setup():
    size(1000,200)
    noStroke()

def draw():
    global x,y,dy,flag
    fill(0,10)
    rect(0,0,width,height)
    x += 2
    if x > width+5:
        x = -5
    if frameCount % 100 == 0:
        flag = not flag
    if flag:
        if y <= 60 or y >= 160:
            dy *= -1
        y += dy
        if y >= 160:
            flag = False
    fill(0,255,0)
    ellipse(x,y,10,10)
