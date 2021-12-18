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
            count = int(random(120,150))
        else:
            isShow = True
            count = int(random(120,150))
    if isShow:
        ellipse(width/2,height/2,50,50)
