px, py, ps = 0, 0, 0
sx, sy = 0, 0
up, down, left, right = False,False,False,False
rxList = []
ryList = []
status = []
over = False
clear = False
limitBar = 600

def setup():
    global px, py, ps
    size(600, 500)
    px = width/2
    py = height/2
    ps = 30
    for i in range(6):
        rxList.append(75+175*(i%3))
        ryList.append(75+250*(i/3))
        status.append(False)

def draw():
    global px, py, ps, sx, sy, over, clear, limitBar
    background(255)
    for i in range(6):
        if status[i]:
            fill(255, 0, 0)
        else:
            fill(255)
        rect(rxList[i], ryList[i], 100, 100)

    fill(0)
    ellipse(px, py, ps, ps)

    if over:
        textSize(50)
        textAlign(CENTER)
        text("GAME OVER", width/2, height/2)
        return

    if clear:
        textSize(50)
        textAlign(CENTER)
        text("GAME CLEAR", width/2, height/2)
        return

    if keyPressed:
        if up:
            sy -= 1
        if down:
            sy += 1
        if left:
            sx -= 1
        if right:
            sx += 1

    sx *= 0.98
    sy *= 0.98
    px += sx
    py += sy

    for i in range(6):
        if px+ps/2>rxList[i] and px-ps/2<rxList[i]+100 \
        and py+ps/2>ryList[i] and py-ps/2<ryList[i]+100:
            status[i] = True

    if px < ps/2 or px > (width-ps/2) or py < ps/2 or py > (height-ps/2):
        over = True

    count = 0
    for i in range(6):
        if status[i]:
            count = count + 1
    if count == 6:
        clear = True

    fill("#FFC400")
    rect(0, 0, limitBar, 30)
    limitBar -= 1.5
    if limitBar <= 0:
        over = True

def keyPressed():
    global up, down, left, right
    if keyCode == UP:
        up = True
    if keyCode == DOWN:
        down = True
    if keyCode == LEFT:
        left = True
    if keyCode == RIGHT:
        right = True

def keyReleased():
    global up, down, left, right
    if keyCode == UP:
        up = False
    if keyCode == DOWN:
        down = False
    if keyCode == LEFT:
        left = False
    if keyCode == RIGHT:
        right = False
