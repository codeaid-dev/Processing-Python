baseRadius = 10
maxTheta = 0
currentTheta = 0

def setup():
    global maxTheta
    size(1000, 1000)
    colorMode(HSB, 360, 100, 100)
    maxTheta = TWO_PI*20

def draw():
    global currentTheta
    background(0)
    translate(width/2, height/2)
    rotate(frameCount * 0.0002)
    noStroke()
    theta = 0
    while theta < currentTheta:
        r = baseRadius * theta
        x = cos(theta) * r
        y = sin(theta) * r

        hue = map(theta, 0, maxTheta,200, 360) + map(mouseX, 0, width, -60, 60)
        fill(hue % 360, 80, 100)

        radius_size = map(sin(theta * 1.5 + frameCount * 0.05), -1, 1, 10, 20)

        ellipse(x, y, radius_size, radius_size)

        arcStep = 25
        angleStep = arcStep / sqrt(r * r + baseRadius * baseRadius)
        theta += angleStep

    currentTheta += 0.1
    maxR = min(width, height) / 2 - 20
    maxAllowedTheta = maxR / baseRadius
    if currentTheta > maxAllowedTheta:
        currentTheta = maxAllowedTheta
