def setup():
    frameRate(1)

def draw():
    h = hour()
    m = minute()
    s = second()
    print("{}:{}:{}".format(h,m,s))
