x,y,s=0,0,0
count=25
def setup():
    global x,y,s
    size(500,500)
    #x,y=width/count,height/count
    s=width/count
    noStroke()

def draw():
    background(200)
    for i in range(count**2):
        if (i%25)/5%2==0:
            fill(255)
        else:
            fill(0)
        ellipse(s*(i%count)+s/2,s*(i/count)+s/2,s,s)
