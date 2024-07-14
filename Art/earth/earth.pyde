p=0
radius=200
def setup():
    size(500,500)

def draw():
    global p
    background(0)
    noStroke()
    fill(255,150,0)
    ellipse(width/2,height/2,40,40)
    x = width/2 + radius * cos(p*PI/180)
    y = height/2 + radius * sin(p*PI/180)
    fill(0,200,200)
    ellipse(x,y,20,20)
    mx = x + 30 * cos(p*12*PI/180)
    my = y + 30 * sin(p*12*PI/180)
    fill(255)
    ellipse(mx,my,5,5)
    p+=0.1
