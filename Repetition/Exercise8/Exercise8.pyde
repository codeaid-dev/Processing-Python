def setup():
    size(500,500)

def draw():
    background(200)
    s = width/10
    for y in range(10):
        for x in range(10):
            if y % 2 == 0 and x % 2 == 1:
                fill(0)
            elif y % 2 == 1 and x % 2 == 0:
                fill(0)
            else:
                fill(255)
            rect(x*s,y*s,s,s)
