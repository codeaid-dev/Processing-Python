x,y=0,0
points=0
radius=200
def setup():
    size(500,500)
    background(0)

def draw():
    global x,y,points
    #background(0)
    noStroke()
    #fill(255,150,0)
    #ellipse(width/2,height/2,40,40)
    x = width/2 + radius * cos(points*PI/180)
    y = height/2 + radius * sin(points*PI/180)
    #fill(0,200,200)
    #ellipse(x,y,20,20)
    mx = x + 30 * cos(points*12*PI/180)
    my = y + 30 * sin(points*12*PI/180)
    fill(255)
    ellipse(mx,my,5,5)
    points+=0.1
