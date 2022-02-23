x,y,s=0,0,0
count=25
def setup():
    global x,y,s
    size(500,500)
    x,y=width/count,height/count
    s=width/count
    noStroke()

def draw():
    background(200)
    for i in range(count):
        for j in range(count):
            if i/5%2==0:
                if j/5%2==0:
                    fill(255)
                else:
                    fill(0)
            else:
                if j/5%2==1:
                    fill(255)
                else:
                    fill(0)
            ellipse(x*j+s/2,y*i+s/2,s,s)
