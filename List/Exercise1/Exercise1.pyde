def setup():
    size(500,500)

def draw():
    en = [[450,50],[350,150],[250,250],[150,350],[50,450]]
    for d in range(len(en)):
        ellipse(en[d][0],en[d][1],50,50)
