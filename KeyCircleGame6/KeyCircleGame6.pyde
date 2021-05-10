px, py, ps = 0, 0, 0
sx, sy = 0, 0
rxList = []
ryList = []
status = []
over = False
clear = False
limitBar = 600

def setup():
    global px, py, ps, rxList, ryList, status
    size(600, 500)
    px = width/2
    py = height/2
    ps = 30
    for i in range(6):
        rxList.append(75+175*(i%3))
        ryList.append(75+250*(i/3))
        status.append(False)

def draw():
    global px, py, ps, sx, sy, rxList, ryList, status, over, clear, limitBar
    rs = 100
    background(255)
    for i in range(6):
        if status[i]:
            fill(255, 0, 0)
        else:
            fill(255)
        rect(rxList[i], ryList[i], rs, rs)

    fill("#FFC400")
    rect(0, 0, limitBar, 30)
    limitBar -= 1.5
    if limitBar <= 0:
        over = True

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
        if keyCode == UP:
            sy -= 1
        if keyCode == DOWN:
            sy += 1
        if keyCode == LEFT:
            sx -= 1
        if keyCode == RIGHT:
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
