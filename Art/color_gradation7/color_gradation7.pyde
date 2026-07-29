class Ball:
    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.d = d
balls = []

def setup():
    size(500,500)
    noStroke()
    for i in range(20):
        balls.append(Ball(
            random(25,width-25),
            random(25,height-25),
            50))

def draw():
    background(255)
    for b in balls:
        drawBall(b.x,b.y,b.d)

def drawBall(x, y, d):
    f = color(255);
    t = color(0);
    for i in range(d,0,-1):
        amt = map(i,0,d,0.0,1.0);
        c = lerpColor(f,t,amt);
        fill(c);
        ellipse(x,y,i,i);
