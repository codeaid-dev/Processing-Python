class Drop:
    def __init__(self):
        self.r=8
        self.x=random(width)
        self.y=-self.r*5
        self.speed=random(1,5)
        self.c=color(0,200,200)

    def move(self):
        self.y+=self.speed

    def is_bottom(self):
        return self.y>height+self.r

    def display(self):
        fill(self.c)
        noStroke()
        for i in range(2,self.r):
            #fill(self.c,(i-2)*40)
            ellipse(self.x,self.y+i*4,i*2,i*2)

drops=[]

def setup():
    size(500,500)

def draw():
    background(255)
    if len(drops) <= 100:
        drops.append(Drop())
    for d in drops:
        d.move()
        d.display()
        if d.is_bottom():
            d.x=random(width)
            d.y=-d.r*5
