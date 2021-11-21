x,y = [],[]
def setup():
    size(500,500)
    for i in range(5):
        x.append(random(25,width-25))
        y.append(random(25,height-25))

def draw():
    background(255)
    for i in range(5):
        fill(0)
        ellipse(x[i],y[i],50,50)
    
