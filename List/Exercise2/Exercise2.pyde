seasons = ['Spring','Summer','Autumn','Winter']

def setup():
    size(600,400)
    textSize(30)
    fill(0)

def draw():
    background(255)
    for i in range(len(seasons)):
        text(seasons[i],i*width/4+30,(i+1)*height/4-50)
