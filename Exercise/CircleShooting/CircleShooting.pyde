x,y = 250,770
bx,by,bs = [],[],[]
def setup():
    size(500,800)
    noStroke()

def draw():
    global x,y
    background(255)
    fill(0,0,255)
    ellipse(x,y,50,50)

    if keyPressed:
        if keyCode == RIGHT:
            x += 3
        if keyCode == LEFT:
            x -= 3
        if keyCode == UP:
            y -= 3
        if keyCode == DOWN:
            y += 3
    if x < 0:
        x += 3
    if x > width:
        x -= 3
    if y < 0:
        y += 3
    if y > height:
        y -= 3


    if frameCount % 10 == 0:
        bx.append(random(width))
        by.append(0)
        bs.append(random(10,50))

    for i in range(len(bx)):
        by[i] += 5
        fill(0)
        ellipse(bx[i],by[i],bs[i],bs[i])
