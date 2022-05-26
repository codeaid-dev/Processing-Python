xList = []
yList = []
s = 30
atari = 0
clear = False

def setup():
    global s, atari
    size(450, 450)
    for i in range(225):
        xList.append(s * (i % 15))
        yList.append(s * (i / 15))
    atari = int(random(225))

def draw():
    global s, atari, clear
    for i in range(225):
        if i == atari and clear:
            fill(255, 0, 0)
        else:
            fill(255)
        rect(xList[i], yList[i], s, s)

    if mousePressed:
        if xList[atari]<mouseX<xList[atari]+s and yList[atari]<mouseY<yList[atari]+s:
            clear = True
