def setup():
    size(600,300)

def draw():
    background(255)
    list1 = [[255,0,0],[0,255,0],[0,0,255]]
    for i in range(12):
        c = i%3
        fill(list1[c][0],list1[c][1],list1[c][2])
        ellipse(25+i*50, height/2, 50, 50)
