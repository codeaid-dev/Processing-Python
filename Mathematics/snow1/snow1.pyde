class Snow:
    def __init__(self):
        self.x = random(width)
        self.y = random(-height,height)
        self.speed = random(1,3)
        self.radius = random(1,3)
        self.wind = random(-0.5,0.5)

    def update(self):
        self.x += self.wind
        self.y += self.speed
        if self.y > height:
            self.y = random(-50,0)
            self.x = random(width)
        if self.x < 0:
            self.x = width
        elif self.x > width:
            self.x = 0

    def draw(self):
        noStroke()
        fill(255)
        circle(self.x,
               self.y,
               self.radius*2)

snows = []

def setup():
    size(600,600)
    for i in range(200):
        snows.append(Snow())

def draw():
    background(0)
    for snow in snows:
        snow.update()
        snow.draw()
