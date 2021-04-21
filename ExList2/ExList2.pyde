s, m = 100, 50
colors = [[255,255,255], [255,255,255], [255,255,255]]
atari = int(random(3))
def setup():
    size(500, 200)

def draw():
    background(0)
    for i in range(3):
        fill(colors[i][0], colors[i][1], colors[i][2])
        rect(i*(s+m)+m, m, s, s)

def mouseClicked():
    for i in range(3):
        if i*(s+m)+m < mouseX < i*(s+m)+m+s:
            if i == atari:
                colors[i] = [255,0,0]
            else:
                colors[i]=[255,255,255]
