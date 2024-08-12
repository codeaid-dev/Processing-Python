x,y=0,0
dx,dy=0,0
s=30
def setup():
    global x,y,dx,dy
    size(600,600)
    x = width/2
    y = height/2
    dx = int(random(2,6))
    dy = int(random(2,6))

def draw():
    global x,y,dx,dy
    background(255)
    x += dx
    y += dy
    if x < s/2 or x > width-s/2:
        dx *= -1
    if y < s/2 or y > height-s/2:
        dy *= -1
    noStroke()
    fill(0,255,0)
    ellipse(x,y,s,s)
