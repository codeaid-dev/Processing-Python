class Ball:
    def __init__(self, r):
        self.r = r
        self.x = random(self.r,width-self.r)
        self.y = random(self.r,height-self.r)
        self.xspeed = random(-5,5)
        self.yspeed = random(-5,5)
        self.c = color(100,50)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x+self.r>width or self.x-self.r<0:
            self.xspeed *= -1
        if self.y+self.r>height or self.y-self.r<0:
            self.yspeed *= -1

    def display(self):
        stroke(0)
        fill(self.c)
        ellipse(self.x,self.y,self.r*2,self.r*2)
        self.c = color(100,50)

    def highlight(self):
        self.c = color(0,150)

    def intersect(self,b):
        distance = dist(self.x,self.y,b.x,b.y)
        if distance<self.r+b.r:
            return True
        else:
            return False

ball1,ball2 = None,None

def setup():
    global ball1,ball2
    size(500,500)
    ball1 = Ball(64)
    ball2 = Ball(32)

def draw():
    background(255)
    ball1.move()
    ball2.move()
    if ball1.intersect(ball2):
        ball1.highlight()
        ball2.highlight()
    ball1.display()
    ball2.display()
