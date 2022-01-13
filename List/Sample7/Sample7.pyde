def setup():
    size(300,300)

def draw():
    background(255)
    color = [[255,0,0],[0,255,0],[0,0,255]]
    for i in range(len(color)):
        fill(color[i][0],color[i][1],color[i][2])
        ellipse(50+i*100, height/2, 50, 50)
