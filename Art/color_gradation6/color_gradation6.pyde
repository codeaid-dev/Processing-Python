def setup():
    size(500,500)
    noStroke()

def draw():
    background(255)
    drawBall(width/2,height/2,200)

def drawBall(x, y, d):
    f = color(255)
    t = color(0)
    for i in range(d,0,-1):
        amt = map(i,0,d,0.0,1.0)
        c = lerpColor(f,t,amt)
        fill(c)
        ellipse(x,y,i,i)
