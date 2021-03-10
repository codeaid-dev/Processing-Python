places = []
cnt = 0

def setup():
    global places, cnt
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

def draw():
    global places, cnt
    background(255)
    for i in range(cnt):
        ellipse(places[i][0], places[i][1], 50, 50)
        places[i][0] += places[i][2]
        if places[i][0] < 25 or places[i][0] > 575:
            places[i][2] *= -1
    
