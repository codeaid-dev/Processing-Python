def setup():
    size(300, 300)

def draw():
    w, h = 10, 10
    for i in range(30):
        rect(w*i, h*i, w, h)
