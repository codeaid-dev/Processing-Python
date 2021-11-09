count = 100
starX = []
starY = []

def setup():
    global count, starX, starY
    size(600, 400)
    for i in range(count):
        starX.append(random(width))
        starY.append(random(height))

def draw():
    global count, starX, starY
    background(0)
    for i in range(count):
        noStroke()
        ellipse(starX[i], starY[i], 5, 5)
