x,y,theta = 0,0,0
r = 200
def setup():
    size(500,500)

def draw():
    global x,y,r,theta
    background(255)
    fill(0,255,255)
    noStroke()
    ellipse(width/2,height/2,50,50)
    fill(200)
    ellipse(x+width/2,y+height/2,50,50)
    x = r*cos(theta*PI/180)
    y = r*sin(theta*PI/180)
    theta += 1
