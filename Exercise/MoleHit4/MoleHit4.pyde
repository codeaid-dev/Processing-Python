count = []
isShow = []
x,y = [],[]
score = 0
def setup():
    size(500,500)
    for i in range(5):
        x.append(random(25,width-25))
        y.append(random(25,height-25))
        count.append(int(random(120,150)))
        isShow.append(False)

def draw():
    global count,isShow
    background(255)
    fill(0)
    for i in range(5):
        count[i] -= 1
        if count[i] == 0:
            if isShow[i]:
                isShow[i] = False
                count[i] = int(random(120,150))
            else:
                isShow[i] = True
                count[i] = int(random(120,150))
        if isShow[i]:
            ellipse(x[i],y[i],50,50)

        textAlign(CENTER)
        textSize(50)
        text('Score: '+str(score),width/2,70)

def mousePressed():
    global count,isShow, score
    for i in range(5):
        dst = dist(mouseX,mouseY,x[i],y[i])
        if dst < 25:
            if isShow[i]:
                score += 1
            isShow[i] = False
            count[i] = int(random(120,150))
