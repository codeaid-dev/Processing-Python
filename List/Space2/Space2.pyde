count = 100
starX = []
starY = []
starS = []

def setup():
    size(600, 400)
    for i in range(count):
        starX.append(random(width))
        starY.append(random(height))
        starS.append(random(1,6))

def draw():
    background(0)
    for i in range(count):
        starX[i] -= starS[i]
        noStroke()
        ellipse(starX[i], starY[i], starS[i], starS[i])
