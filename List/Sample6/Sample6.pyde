def setup():
    size(500,500)

def draw():
    background(255)
    pos = [[125,250,375],[250,250,250]]
    for i in range(3):
        fill(0)
        ellipse(pos[0][i],pos[1][i],100,100)
