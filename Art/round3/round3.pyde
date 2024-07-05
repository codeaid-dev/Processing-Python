points=0
radius=1
dr=0.1
def setup():
    size(500,500)

def draw():
    global points,radius,dr
    fill(0,10)
    rect(0,0,width,height)
    noStroke()
    fill(255,200,0)
    ellipse(width/2,height/2,30,30)
    x = width/2+radius*cos(points*PI/180)
    y = height/2+radius*sin(points*PI/180)
    fill(0,200,200)
    ellipse(x,y,10,10)
    points+=1
    radius+=dr
    if radius > width/2 or radius > height/2:
        dr = -0.5
    if radius < 0:
        dr = 0.1
