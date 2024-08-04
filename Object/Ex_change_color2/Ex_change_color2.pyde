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
atari = 0
dr,dg,db = 0.1,0.1,0.1
def setup():
    global atari
    size(400,400)
    for i in range(16):
        en = Circle(50+i%4*100,50+i/4*100,100)
        balls.append(en)
    atari = int(random(16))

def draw():
    global dr,dg,db
    balls[atari].r += dr
    if balls[atari].r < 0 or balls[atari].r > 255:
        dr *= -1
    balls[atari].g += dg
    if balls[atari].g < 0 or balls[atari].g > 255:
        dg *= -1
    balls[atari].b += db
    if balls[atari].b < 0 or balls[atari].b > 255:
        db *= -1
    for b in balls:
        b.display()
