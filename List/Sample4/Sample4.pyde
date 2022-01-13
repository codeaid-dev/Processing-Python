def setup():
    size(600,300)

def draw():
    background(255)
    data = [135,253,90,52]
    color = [128,80,100,200]
    x = 35
    for i in range(4):
        fill(color[i])
        rect(x, height/2-25, data[i], 50)
        x += data[i]
