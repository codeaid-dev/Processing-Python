def setup():
    size(500,500)

def draw():
    background(255)
    x = [200,350,450,150]
    y = [100,400,200,300]
    s = [30,100,50,200]
    for i in range(4):
        fill(0)
        ellipse(x[i], y[i], s[i], s[i])
