x,y = [],[]
def setup():
    size(500, 500)
    background(255)

def draw():
    overlay()
    fill(180,240,255)
    for i in reversed(range(len(y))):
        ellipse(x[i], y[i], 5, 5)
        x[i] = x[i] + random(-1, 1)
        y[i] = y[i] + random(1, 3)
        if y[i] > height:
            del y[i]
            del x[i]

def overlay():
    fill(255, 30)
    noStroke()
    rect(0,0,width,height)

def mousePressed():
    x.append(mouseX)
    y.append(mouseY)
