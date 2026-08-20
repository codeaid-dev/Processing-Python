class Snow:
    def __init__(self):
        self.x = random(width)
        self.y = random(-height,height)
        self.speed = random(1,3)
        self.radius = random(1,3)

        self.angle = random(TWO_PI)
        self.swing1 = random(0.01,0.03)
        self.swing2 = random(0.5,2)

    def update(self):
        self.y += self.speed
        self.angle += self.swing1
        self.x += sin(self.angle)*self.swing2
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
