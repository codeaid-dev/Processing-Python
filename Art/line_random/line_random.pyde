x, y = 0, 0
up, bottom = 50,-50
def setup():
    size(500,500)
    x = random(width)
    y = random(height)

def draw():
    global x,y
    dx = random(bottom,up)
    dy = random(bottom,up)
    while x+dx < 0 or x+dx > width:
        dx = random(bottom,up)
    while y+dy < 0 or y+dy > height:
        dy = random(bottom,up)
    line(x,y,x+dx,y+dy)
    x += dx
    y += dy
