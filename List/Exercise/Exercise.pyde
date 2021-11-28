def setup():
    size(500,500)

def draw():
    en = [[450,50],[350,150],[250,250],[150,350],[50,450]]
    for d in en:
        ellipse(d[0],d[1],50,50)
