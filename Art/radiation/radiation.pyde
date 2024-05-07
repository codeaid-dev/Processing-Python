ens = []

class Circle:
    pass
r = 0
speed = 0.5
def setup():
    size(600,600)
    for i in range(18):
        c = Circle()
        c.x = width/2
        c.y = height/2
        ens.append(c)

def draw():
    global r, speed
    background(0)
    fill(255)
    noStroke()
    r += speed
    for i,c in enumerate(ens):
        c.x = width/2+r*cos(radians(i*20))
        c.y = height/2+r*sin(radians(i*20))
#        c.x += cos(radians(i*20))
#        c.y += sin(radians(i*20))
        ellipse(c.x,c.y,10,10)
    #stroke(255,128)
    #noFill()
    #ellipse(width/2,height/2,r*2,r*2)
    if r > width-5 or r < 0:
        speed *= -1
        
