xList = [None, None, None, None]
yList = [None, None, None, None]

def setup():
    size(600, 400)

def draw():
    global xList, yList
    background(255)
    fill(0)
    rectMode(CENTER)
    for i in range(4):
        xList[i] = 90 + 140 * (i % 4)
        yList[i] = 200
        rect(xList[i], yList[i], 100, 100)
