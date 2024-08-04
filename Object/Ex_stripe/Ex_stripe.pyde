class Stripe:
    def __init__(self):
        self.x = 0
        self.speed = random(1)
        self.w = random(30,100)
        self.mouse = False

    def display(self):
        if self.mouse:
            fill(255,0,0)
        else:
            fill(255,100)
        noStroke()
        rect(self.x,0,self.w,height)

    def move(self):
        self.x += self.speed
        if self.x>width:
            self.x = -self.w

    def rollover(self,mx):
        if mx>self.x and mx<self.x+self.w:
            self.mouse = True
        else:
            self.mouse = False

stripes = []

def setup():
    global stripes
    size(500,500)
    for i in range(10):
        stripes.append(Stripe())

def draw():
    background(100)
    for s in stripes:
        s.rollover(mouseX)
        s.move()
        s.display()
