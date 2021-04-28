def setup():
    size(300,300)

def draw():
    background(255)
    list1 = [[255,0,0],[0,255,0],[0,0,255]]
    for i in range(3):
        fill(list1[i][0],list1[i][1],list1[i][2])
        ellipse(50+i*100, height/2, 50, 50)
