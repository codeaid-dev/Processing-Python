count = int(random(120,150))
isShow = False
def setup():
    size(500,500)

def draw():
    global count,isShow
    background(255)
    fill(0)
    count -= 1
    if count == 0:
        if isShow:
            isShow = False
        else:
            isShow = True
        count = int(random(120,150))
    if isShow:
        ellipse(width/2,height/2,50,50)

def mousePressed():
    global count,isShow
    dst = dist(mouseX,mouseY,width/2,height/2)
    if dst < 25:
        isShow = False
        count = int(random(120,150))
