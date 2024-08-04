class Circle:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s
        self.r = random(256)
        self.g = random(256)
        self.b = random(256)

    def display(self):
        fill(self.r,self.g,self.b)
        ellipse(self.x,self.y,self.s,self.s)

balls = []
def setup():
    size(400,400)
    for i in range(16):
        en = Circle(50+i%4*100,50+i/4*100,100)
        balls.append(en)

def draw():
    for b in balls:
        b.display()
