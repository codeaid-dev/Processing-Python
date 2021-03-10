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
    global xList, yList, atari, gameOver, gameClear
    background(255)
    fill(0)
    rectMode(CENTER)
    for i in range(4):
        xList[i] = 90 + 140 * (i % 4)
        yList[i] = 200
        rect(xList[i], yList[i], 100, 100)

    if gameOver:
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER", width/2, 100)
        return

    if gameClear:
        fill(255, 0, 0)
        ellipse(xList[atari], yList[atari], 100, 100)
        return

    if mousePressed:
        if mouseX < xList[atari] + 50 and mouseX > xList[atari] - 50 \
        and mouseY < yList[atari] + 50 and mouseY > yList[atari] - 50:
            gameClear = True
        else:
            gameOver = True
