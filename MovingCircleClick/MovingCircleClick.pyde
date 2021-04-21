places = []
cnt = 0
status = []

def setup():
    global places, cnt, status
    size(600, 200)
    cnt = int(random(10))+1
    for i in range(cnt):
        work = [None,None,None]
        if int(random(2)) % 2 == 0:
            work[2] = -int(random(10))
        else:
            work[2] = int(random(10))
        work[0] = width/2
        work[1] = random(height)
        places.append(work)
        status.append(0)

def draw():
    global places, cnt, status
    background(255)
    for i in range(cnt):
        if status[i] == 1:
            fill(255,0,0)
        else:
            fill(255)
        ellipse(places[i][0], places[i][1], 50, 50)
        places[i][0] += places[i][2]
        if places[i][0] < 25 or places[i][0] > 575:
            places[i][2] *= -1

    if mousePressed:
        isHit()

def isHit():
    global places, cnt, status
    for i in range(cnt):
        dis = dist(mouseX, mouseY, places[i][0], places[i][1])
        if dis < 25:
            places[i][2] = 0
            status[i] = 1
            return True
    return False
