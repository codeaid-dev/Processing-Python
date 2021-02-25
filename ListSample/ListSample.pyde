count = 100
speed = 1
starX = []
starY = []

def setup():
    global count, speed, starX, starY
    size(600, 400)
    for i in range(count):
        starX.append(random(width))
        starY.append(random(height))

def draw():
    background(0)
    for i in range(count):
        x = starX[i]
        x = x - speed
        if x < 0:
            x = width
        starX[i] = x
        noStroke()
        ellipse(starX[i], starY[i], 5, 5)
    
