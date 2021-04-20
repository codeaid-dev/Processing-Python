y = 0
s = 10

def setup():
    size(200, 500)

def draw():
    global y, s
    background(255)
    y += 2
    s += 1
    fill(255,0,0)
    ellipse(width/2, y, s, s)
    
