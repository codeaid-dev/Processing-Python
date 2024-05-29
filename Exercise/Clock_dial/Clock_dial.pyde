def setup():
    size(500,500)

def draw():
    background(0)
    margin = 20
    fill(200)
    for i in range(60):
        x = width/2 + (width/2-margin) * cos(radians(i*6))
        y = height/2 + (width/2-margin) * sin(radians(i*6))
        ellipse(x,y,5,5)
    for i in range(12):
        x = width/2 + (width/2-margin) * cos(radians(i*30))
        y = height/2 + (width/2-margin) * sin(radians(i*30))
        ellipse(x,y,20,20)
