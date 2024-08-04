class Triangle:
    def __init__(self,x1,y1,x2,y2,x3,y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.dx1 = int(random(2,4))
        self.dy1 = int(random(3,5))
        self.dx2 = int(random(2,4))
        self.dy2 = int(random(3,5))
        self.dx3 = int(random(2,4))
        self.dy3 = int(random(3,5))
        self.c = color(random(255),
                       random(255),
                       random(255),
                       random(255))

    def draw(self):
        self.x1 += self.dx1
        self.y1 += self.dy1
        self.x2 += self.dx2
        self.y2 += self.dy2
        self.x3 += self.dx3
        self.y3 += self.dy3
        if self.x1 > width or self.x1 < 0:
            self.dx1 *= -1
        if self.x2 > width or self.x2 < 0:
            self.dx2 *= -1
        if self.x3 > width or self.x3 < 0:
            self.dx3 *= -1
        if self.y1 > height or self.y1 < 0:
            self.dy1 *= -1
        if self.y2 > height or self.y2 < 0:
            self.dy2 *= -1
        if self.y3 > height or self.y3 < 0:
            self.dy3 *= -1
        fill(self.c)
        triangle(self.x1,self.y1,self.x2,self.y2,self.x3,self.y3)

tris =  []
def setup():
    size(500,500)
    for i in range(50):
        tri = Triangle(random(50,450),
                   random(50,450),
                   random(50,450),
                   random(50,450),
                   random(50,450),
                   random(50,450))
        tris.append(tri)
    noStroke()

def draw():
    background(0)
    for tri in tris:
        tri.draw()
