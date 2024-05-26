def setup():
    size(600,600)

def draw():
    background(255)
    for i in range(16):
        ellipse(i%4*150+75,i/4*150+75,150,150)
