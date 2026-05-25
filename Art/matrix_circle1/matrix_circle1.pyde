def setup():
    size(500,500)
    noStroke()
    
def draw():
    background(255)
    for i in range(9):
        for j in range(9):
            fill(random(255),random(255),random(255))
            ellipse(50+j*50,50+i*50,40,40)
