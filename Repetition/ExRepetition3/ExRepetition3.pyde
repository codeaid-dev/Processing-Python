s = 40
def setup():
    size(500, 500)

def draw():
    global s
    for x in range(11):
        for y in range(11):
            if x*s+50 == 250 or y*s+50 == 250:
                fill(0)
            else:
                fill(255)
            ellipse(x*s+50, y*s+50, s, s)
