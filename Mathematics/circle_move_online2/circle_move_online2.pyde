x1,y1 = 100,100
x2,y2 = 400,400
status = True
circleX,circleY = x1,y1
def setup():
    size(500,500)

def draw():
    global circleX,circleY,status
    background(255)
    strokeWeight(3)
    stroke(200)
    line(x1,y1,x2,y2)
    
    noStroke()
    fill(0)
    ellipse(circleX,circleY,60,60)
    if status:
        dx = x2 - circleX
        dy = y2 - circleY
        if dist(circleX,circleY,x2,y2) < 1:
            status = False
    else:
        dx = x1 - circleX
        dy = y1 - circleY
        if dist(circleX,circleY,x1,y1) < 1:
            status = True
    angle = atan2(dy,dx)
    circleX += cos(angle)*2
    circleY += sin(angle)*2
