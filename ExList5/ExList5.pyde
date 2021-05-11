count = 100
xList = []
yList = []
statusList = []
sizeList = []
colorList = []

def setup():
    global count, xList, yList, sizeList, colorList
    size(600, 400)
    for i in range(count):
        xList.append(0)
        yList.append(random(height))
        statusList.append(0)
        sizeList.append(random(10,30))
        colorList.append([random(256),random(256),random(256)])

def draw():
    global count, xList, yList, sizeList, colorList
    background(0)
    for i in range(count):
        if statusList[i] == 1:
            xList[i] += 1
            noStroke()
            fill(colorList[i][0],colorList[i][1],colorList[i][2])
            ellipse(xList[i], yList[i], sizeList[i], sizeList[i])

def mouseClicked():
    global count, statusList
    for i in range(count):
        if statusList[i] == 0:
            statusList[i] = 1
            break
