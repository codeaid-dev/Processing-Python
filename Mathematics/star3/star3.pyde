def setup():
    size(500,500)

def draw():
    background(255)
    fill(255,255,0)
    pushMatrix()
    translate(width/2,height/2)
    rotate(-90*PI/180)
    star(0,0,100,40,5)
    popMatrix()

def star(x,y,radius1,radius2,n):
    angle = TWO_PI/(n*2)
    beginShape()
    for i in range(n*2):
        if i % 2 == 0:
            radius = radius1
        else:
            radius = radius2
        sx = x+radius*cos(i * angle)
        sy = y+radius*sin(i * angle)
        vertex(sx,sy)
    endShape(CLOSE)
