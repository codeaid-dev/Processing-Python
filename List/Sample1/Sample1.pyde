def setup():
    size(600, 400)

def draw():
    weeks = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    background(255)
    for i in range(len(weeks)):
        fill(0)
        textSize(30)
        textAlign(CENTER)
        text(weeks[i], 75+i*75, 200)
