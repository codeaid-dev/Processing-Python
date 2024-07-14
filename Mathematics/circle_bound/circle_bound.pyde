dir = int(random(360))
x,y = 250,250
speed = 5
def setup():
    size(500,500)

def draw():
    global x,y,dir
    background(255)
    x += speed * cos(radians(dir))
    y += speed * sin(radians(dir))
    fill(0)
    ellipse(x,y,30,30)
    if x < 15 or x > width-15:
        dir = 180-dir
    if y < 15 or y > height-15:
        dir *= -1
