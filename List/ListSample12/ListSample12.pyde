xList = [None, None, None, None]
yList = [None, None, None, None]
atari = 0

def setup():
    global atari
    size(600, 400)
    atari = int(random(4))

def draw():
    global xList, yList, atari
    background(255)
    fill(0)
    rectMode(CENTER)
    for i in range(4):
        xList[i] = 90 + 140 * (i % 4)
        yList[i] = 200
        rect(xList[i], yList[i], 100, 100)

    if mousePressed:
        if mouseX < xList[atari] + 50 and mouseX > xList[atari] - 50 \
        and mouseY < yList[atari] + 50 and mouseY > yList[atari] - 50:
            textSize(50)
            textAlign(CENTER)
            text("Atari", width/2, 100)
        else:
            textSize(50)
            textAlign(CENTER)
            text("Hazure", width/2, 100)
