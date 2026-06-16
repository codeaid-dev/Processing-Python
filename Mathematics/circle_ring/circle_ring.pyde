class Circle:
    pass

index = 0
ens = []
def setup():
    size(500,500)
    for i in range(360):
        x = width/2 + 200 * cos(i*PI/180)
        y = height/2 + 200 * sin(i*PI/180)
        for _ in range(4):
            en = Circle()
            en.d = random(2,5)
            en.x = random(x-30,x+30)
            en.y = random(y-30,y+30)
            ens.append(en)
    background(0)

def draw():
    global index
    noStroke()
    #fill(0,10)
    #rect(0,0,width,height)
    fill(0,255,0)
    for _ in range(2):
        ellipse(ens[index].x,ens[index].y,
                ens[index].d,ens[index].d)
        index = (index+1)%1440
