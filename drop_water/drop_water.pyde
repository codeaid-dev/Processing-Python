x = [0 for i in range(100)]
y = [0 for i in range(100)]
number = 0
def setup():
    size(500, 500)
    background(255)

def draw():
    overlay()
    fill(0,220,255)
    for i in range(number):
        ellipse(x[i], y[i], 5, 5)
        x[i] = x[i] + random(-1, 1)
        y[i] = y[i] + random(1, 3)

def overlay():
    fill(255, 30)
    noStroke()
    rect(0,0,width,height)

def mousePressed():
    global number
    x[number] = mouseX
    y[number] = mouseY
    number += 1
