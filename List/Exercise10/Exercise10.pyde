ens = []
count = 0

def setup():
    size(600, 400)

def draw():
    background(0)
    for p in range(len(ens)):
        ens[p][0] += 1
        noStroke()
        fill(ens[p][3][0],ens[p][3][1],ens[p][3][2])
        ellipse(ens[p][0],ens[p][1],ens[p][2],ens[p][2])

def mousePressed():
    global ens,count
    if count < 50:
        en = [0,random(height),random(10,30)]
        en.append([random(256),random(256),random(256)])
        ens.append(en)
        count += 1
