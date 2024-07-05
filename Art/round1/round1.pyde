p=0
radius=200
def setup():
    size(500,500)

def draw():
    global p
    background(255)
    noStroke()
    fill(255,200,0)
    ellipse(width/2,height/2,30,30)
    x = width/2 + radius * cos(p*PI/180)
    y = height/2 + radius * sin(p*PI/180)
    fill(0,200,200)
    ellipse(x,y,50,50)
    p+=1
