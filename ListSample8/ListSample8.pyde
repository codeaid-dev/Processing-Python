count = 100
speed = []
starX = []
starY = []

def setup():
    global count, speed, starX, starY
    size(600, 400)
    for i in range(count):
        starX.append(random(width))
        starY.append(random(height))
        speed.append(random(1,6))

def draw():
    global count, speed, starX, starY
    background(0)
    for i in range(count):
        x = starX[i]
        x = x - speed[i]
        if x < 0:
            x = width
        starX[i] = x
        noStroke()
        fill(255, 255, 255, speed[i]/5*255)
        ellipse(starX[i], starY[i], 5, 5)
    
