def setup():
    size(500, 500)

def draw():
    background(255)
    for i in range(9):
        for j in range(9):
            textAlign(CENTER)
            fill(0)
            ans = (i+1)*(j+1)
            text(str(i+1)+"x"+str(j+1)+"="+str(ans), 25+j*55, 25+i*55)
