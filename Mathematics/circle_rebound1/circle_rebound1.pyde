numCircles = 10
circles = [None for i in range(numCircles)]

def setup():
    size(800, 600)
    for i in range(numCircles):
        circles[i] = Circle(random(width), random(height), random(20, 50))

def draw():
    background(255)
    
    for i in range(numCircles):
        circles[i].move()
        circles[i].checkBoundaryCollision()
        circles[i].checkCircleCollision(circles)
        circles[i].display()

class Circle:
    def __init__(self, x, y, radius):
        self.x = x; # x座標
        self.y = y; # y座標
        self.radius = radius; # 半径
        self.vx = random(-2, 2); # x速度
        self.vy = random(-2, 2); # y速度

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def checkBoundaryCollision(self):
        if self.x-self.radius < 0 or self.x+self.radius > width:
            self.vx *= -1;
            if self.x-self.radius<0: self.x=self.radius
            if self.x+self.radius>width: self.x=width-self.radius
        if self.y-self.radius < 0 or self.y+self.radius > height:
            self.vy *= -1;
            if self.y-self.radius<0: self.y=self.radius
            if self.y+self.radius>height: self.y=height-self.radius

    def checkCircleCollision(self, circles):
        for i in range(len(circles)):
            other = circles[i]
            if other != self:
                dx = other.x - self.x
                dy = other.y - self.y
                distance = sqrt(dx * dx + dy * dy)
                minDist = self.radius + other.radius
    
                if distance < minDist:
                    # 当たり判定があった場合、反射する
                    angle = atan2(dy, dx)
                    targetX = self.x + cos(angle) * minDist
                    targetY = self.y + sin(angle) * minDist
                    ax = (targetX - other.x) * 0.05
                    ay = (targetY - other.y) * 0.05
                    self.vx -= ax;
                    self.vy -= ay;
                    other.vx += ax;
                    other.vy += ay;

    def display(self):
        fill(150, 100, 200, 150)
        noStroke()
        ellipse(self.x, self.y, self.radius*2, self.radius*2)
