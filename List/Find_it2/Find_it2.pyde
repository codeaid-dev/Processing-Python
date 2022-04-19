xList = [None, None, None, None]
yList = [None, None, None, None]
atari = 0

def setup():
    global atari
    size(600, 400)
    atari = int(random(4))

def draw():
    background(255)
    fill(0)
    for i in range(4):
        xList[i] = 40 + 140 * i
        yList[i] = 150
        rect(xList[i], yList[i], 100, 100)

    if mousePressed:
        if mouseX>xList[atari] and mouseX<xList[atari]+100 \
            and mouseY>yList[atari] and mouseY<yList[atari]+100:
            textSize(50)
            textAlign(CENTER)
            text("Atari", width/2, 100)
        else:
            textSize(50)
            textAlign(CENTER)
            text("Hazure", width/2, 100)
