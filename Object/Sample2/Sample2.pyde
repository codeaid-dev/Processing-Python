circles = []
class Circle:
    def reset(self):
        self.x = random(width)
        self.y = random(height)
        self.s = random(30)
        self.iro = color(random(256),random(256),random(256))

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
        c.s += 0.5
        if c.s > 30:
            c.s = 0
        fill(c.iro)
        ellipse(c.x,c.y,c.s,c.s)
