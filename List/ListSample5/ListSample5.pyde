paints = [None, None, None, None, None]
placeX = [None, None, None, None, None]
placeY = [None, None, None, None, None]
def setup():
    global paints, placeX, placeY
    size(500, 500)
    for i in range(5):
        paints[i] = [random(256), random(256), random(256)]
        placeX[i] = random(width)
        placeY[i] = random(height)

def draw():
    global paints, placeX, placeY
    background(0)
    for i in range(5):
        fill(paints[i][0], paints[i][1], paints[i][2])
        ellipse(placeX[i], placeY[i], 100, 100)
