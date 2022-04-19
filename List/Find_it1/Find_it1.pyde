xList = [None, None, None, None]
yList = [None, None, None, None]

def setup():
    size(600, 400)

def draw():
    #global xList, yList
    background(255)
    fill(0)
    for i in range(4):
        xList[i] = 40 + 140 * i
        yList[i] = 150
        rect(xList[i], yList[i], 100, 100)
