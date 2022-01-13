x,y = [],[]
count = 0
def setup():
    size(500, 500)

def draw():
    fill(255, 30)
    noStroke()
    rect(0,0,width,height)
    fill(180,240,255)
    for i in range(len(y)):
        ellipse(x[i], y[i], 5, 5)
        x[i] = x[i] + random(-1, 1)
        y[i] = y[i] + random(1, 3)

def mousePressed():
    global count
    if count < 50:
        x.append(mouseX)
        y.append(mouseY)
        count += 1
