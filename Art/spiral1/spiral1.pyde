class Circle:
    def show(self):
        fill(0)
        ellipse(self.x,self.y,10,10)

circles = []
def setup():
    size(500,500)
    angle=0
    radius = 0
    while True:
        angle += 0.16
        radius += 0.5
        x = width/2 + radius * cos(angle)
        y = height/2 + radius * sin(angle)
        if x < 0 or x > width or y < 0 or y > height: break
        c = Circle()
        c.x = x
        c.y = y
        circles.append(c)
    noStroke()

def draw():
    background(255)
    for c in circles:
        c.show()
