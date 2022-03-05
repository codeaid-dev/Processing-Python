x,y=0,0
radius=0
def setup():
    size(500,500)

def draw():
    global x,y,radius
    background(255)
    noStroke()
    fill(255,200,0)
    ellipse(width/2,height/2,30,30)
    for i in range(0,360,10):
        x = width/2 + radius * cos(i*PI/180)
        y = height/2 + radius * sin(i*PI/180)
        fill(0,200,200)
        ellipse(x,y,5,5)
    radius+=2
    if radius>200:
        radius=0
