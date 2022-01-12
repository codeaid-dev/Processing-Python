def setup():
    size(500, 500)

def draw():
    background(255)
    for i in range(9):
        for j in range(9):
            textAlign(CENTER)
            textSize(20)
            fill(0)
            ans = (i+1)*(j+1)
            text(ans, 50+j*width/10, 50+i*height/10)
