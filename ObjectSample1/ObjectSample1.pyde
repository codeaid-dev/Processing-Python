circles = []
class Circle:
    def reset(self):
        self.x = random(width)
        self.y = random(height)
        self.vy = random(1,6)
        self.iro = color(random(255),random(255),random(255))

def setup():
    global circles
    size(500,500)
    for i in range(50):
        c = Circle()
        c.reset()
        circles.append(c)

def draw():
    background(0)
    for c in circles:
        c.y += c.vy
        if c.y > height:
            c.y = 0
        fill(c.iro)
        ellipse(c.x,c.y,30,30)
