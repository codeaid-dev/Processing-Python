xList = []
yList = []
s = 30
atari = 0
clear = False

def setup():
    global xList, yList, s, atari
    size(500, 500)
    for i in range(225):
        xList.append(40 + s * (i % 15))
        yList.append(40 + s * (i / 15))
    atari = int(random(225))

def draw():
    global xList, yList, s, atari, clear
    background(0)
    rectMode(CENTER)
    for i in range(225):
        if i == atari and clear:
            fill(255, 0, 0)
        else:
            fill(255)
        rect(xList[i], yList[i], s, s)

    if mousePressed:
        if mouseX < xList[atari] + s / 2 and mouseX > xList[atari] - s / 2 \
        and mouseY < yList[atari] + s / 2 and mouseY > yList[atari] - s / 2:
            clear = True
