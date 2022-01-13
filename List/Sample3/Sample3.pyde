def setup():
    size(500,500)

def draw():
    background(255)
    data = [135,253,90,52]
    line(125,100,125,380)
    for i in range(len(data)):
        fill(128)
        rect(125, 125+60*i, data[i], 50)
