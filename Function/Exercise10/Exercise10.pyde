x,y = [],[]
radius = []

def setup():
    size(500,500)
    noStroke()

def draw():
    background(0)
    for n in range(len(x)):
        fill(255,255,0)
        ellipse(x[n],y[n],radius[n],radius[n])
        
def mousePressed():
    x.append(mouseX)
    y.append(mouseY)
    radius.append(0)

def mouseDragged():
    dst = dist(x[len(x)-1],y[len(y)-1],mouseX,mouseY)
    radius[len(radius)-1] = dst*2
