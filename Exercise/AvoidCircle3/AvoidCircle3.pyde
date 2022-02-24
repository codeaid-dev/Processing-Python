x,y,s = 250,400,50
block_x,block_y,block_size = [],[],[]
def setup():
    size(500,800)
    noStroke()
def draw():
    global x,y
    background(255)

    fill(0,0,255)
    ellipse(x,y,s,s)

    if keyPressed:
        if keyCode == RIGHT:
            x += 3
        if keyCode == LEFT:
            x -= 3
        if keyCode == UP:
            y -= 3
        if keyCode == DOWN:
            y += 3
    
    if x < s/2:
        x += 3
    if x > width-s/2:
        x -= 3
    if y < s/2:
        y += 3
    if y > height-s/2:
        y -= 3

    if frameCount % 10 == 0:
        block_x.append(random(width))
        block_y.append(0)
        block_size.append(random(10,50))
    
    for i in range(len(block_y)):
        block_y[i] += 5
        fill(0)
        ellipse(block_x[i],block_y[i],\
                block_size[i],block_size[i])
