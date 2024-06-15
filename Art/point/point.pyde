def setup():
    size(500,500)
    noLoop()

def draw():
    background(255)
    strokeWeight(10)
    for i in range(360):
        x = width/2 + 200 * cos(radians(i))
        y = height/2 + 200 * sin(radians(i))
        point(x,y)
    for i in range(180):
        x = width/2 + 150 * cos(radians(i))
        y = height/2 + 150 * sin(radians(i))
        point(x,y)

    noStroke()
    fill(0)
    ellipse(width/2-50,height/2-50,50,100)
    ellipse(width/2+50,height/2-50,50,100)
