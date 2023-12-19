places = []
cnt = 8
status = []

def setup():
    size(600, 200)
    for i in range(cnt):
        work = [None,None,None]
        if random(5) / 2 > 1:
            work[2] = -random(1,11)
        else:
            work[2] = random(1,11)
        work[0] = width/2
        work[1] = random(height)
        places.append(work)
        status.append(0)

def draw():
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
        checkHit()

def checkHit():
    for i in range(cnt):
        dis = dist(mouseX, mouseY, places[i][0], places[i][1])
        if dis < 25:
            places[i][2] = 0
            status[i] = 1
