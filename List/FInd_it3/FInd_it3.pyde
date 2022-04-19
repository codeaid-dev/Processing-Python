xList = [None, None, None, None]
yList = [None, None, None, None]
atari = 0
gameOver = False
gameClear = False

def setup():
    global atari
    size(600, 400)
    atari = int(random(4))

def draw():
    global gameOver, gameClear
    background(255)
    fill(0)
    for i in range(4):
        xList[i] = 40 + 140 * i
        yList[i] = 150
        rect(xList[i], yList[i], 100, 100)

    if gameOver:
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER", width/2, 100)
        return

    if gameClear:
        fill(255, 0, 0)
        ellipse(xList[atari]+50, yList[atari]+50, 100, 100)
        return

    if mousePressed:
        if mouseX>xList[atari] and mouseX<xList[atari]+100 \
            and mouseY>yList[atari] and mouseY<yList[atari]+100:
            gameClear = True
        else:
            gameOver = True
