def setup():
    size(500,500)

def draw():
    background(200)
    for col in range(9):
        for row in range(col+1):
            x = (width/2-(col-row)*25)+row*25
            y = col*50+25
            fill(255)
            ellipse(x,y,50,50)
