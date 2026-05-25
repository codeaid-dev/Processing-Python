colors = []
def setup():
    size(500,500)
    noStroke()
    for i in range(81):
        colors.append([random(255),
                       random(255),
                       random(255)])

def draw():
    background(255)
    for i in range(81):
        fill(colors[i][0],colors[i][1],colors[i][2])
        ellipse(50+(i%9)*50,50+(i/9)*50,40,40)
