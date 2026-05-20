centerX,centerY = 0,0
def setup():
    global centerX,centerY
    size(500,500)
    background(0)
    stroke(200)
    centerX = width/2
    centerY = height/2

def draw():
    if mousePressed:
        angle = atan2(mouseY-centerY,mouseX-centerX)
        pd = dist(pmouseX,pmouseY,centerX,centerY)
        d = dist(mouseX,mouseY,centerX,centerY)
        i = 0
        while i<TWO_PI:
            px = centerX+pd * cos(angle+i)
            py = centerY+pd * sin(angle+i)
            x = centerX+d * cos(angle+i)
            y = centerY+d * sin(angle+i)
            line(px,py,x,y)
            i += TWO_PI/36
