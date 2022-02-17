ens = []
count = 0

def setup():
    size(600, 400)

def draw():
    background(0)
    for p in range(len(ens)):
        ens[p][0] += 1
        noStroke()
        ellipse(ens[p][0], ens[p][1], 20, 20)

def mousePressed():
    global ens,count
    if count < 50:
        en = [0,random(height)]
        ens.append(en)
        count += 1
