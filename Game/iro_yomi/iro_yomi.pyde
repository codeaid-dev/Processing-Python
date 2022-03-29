en = []
iro = [color(255,0,0),
       color(0,255,0),
       color(0,0,255),
       color(255,255,0)]
moji = ['RED',
        'GREEN',
        'BLUE',
        'YELLOW']
choice = ['yomi',
          'iro']
odai = []
answer = 0
timebar = 600
finish = False
def setup():
    size(600,600)
    en.append(PVector(width/2,height/5))
    en.append(PVector(width/5*4,height/2))
    en.append(PVector(width/2,height/5*4))
    en.append(PVector(width/5,height/2))
    for i in range(2):
       odai.append(int(random(4)))
    odai.append(int(random(2)))

def draw():
    global timebar,finish
    background(200)
    noStroke()
    textSize(30)
    textAlign(CENTER)
    for i in range(4):
        fill(iro[i])
        ellipse(en[i].x,en[i].y,200,200)

    fill(0)
    text(answer,width/5,height/5)

    if finish:
        fill(200,0,0)
        text('FINISH',width/2,height/2)
        return

    fill(iro[odai[0]])
    text(moji[odai[1]],width/2,height/2)
    fill(0)
    text(choice[odai[2]],width/2,height/2+30)

    fill(0,128,128)
    rect(0,0,timebar,10)
    timebar -= 0.3
    if timebar <= 0:
        finish = True

def mousePressed():
    global answer
    if finish:
        return
    x = mouseX
    y = mouseY
    for i in range(4):
        dst = dist(x,y,en[i].x,en[i].y)
        if dst < 100:
            if odai[2] == 0:
                if odai[1] == i:
                    answer += 1
            else:
                if odai[0] == i:
                    answer += 1

            for i in range(2):
                odai[i] = int(random(4))
            odai[2] = int(random(2))
