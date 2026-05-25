en1_x = []
en2_x = []
def setup():
    size(500,500)
    noStroke()
    for i in range(81):
        x = random(-10,10)
        en1_x.append(x)
        x = random(-10,10)
        en2_x.append(x)

def draw():
    background(255)
    for i in range(81):
        fill(150,210,250,180)
        ellipse((50+en1_x[i])+(i%9)*50,
                50+(i/9)*50,
                60,60)

    for i in range(81):
        fill(60,190,255,180)
        ellipse((50+en2_x[i])+(i%9)*50,
                50+(i/9)*50,
                40,40)
