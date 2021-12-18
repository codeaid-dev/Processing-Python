count = 100
xList = []
yList = []
statusList = []

def setup():
    global count, xList, yList
    size(600, 400)
    for i in range(count):
        xList.append(0)
        yList.append(random(height))
        statusList.append(0)

def draw():
    global count, xList, yList
    background(0)
    for i in range(count):
        if statusList[i] == 1:
            xList[i] += 1
            noStroke()
            ellipse(xList[i], yList[i], 20, 20)

def mouseClicked():
    for i in range(count):
        if statusList[i] == 0:
            statusList[i] = 1
            break
