def setup():
    size(500, 500)
    textSize(30)

def draw():
    number = [['One', 'Two', 'Three'], ['Four', 'Five', 'Six'], ['Seven', 'Eight', 'Nine']]
    for i in range(3):
        for j in range(3):
            x = (j+1)*width/4
            y = (i+1)*height/4
            textAlign(CENTER)
            text(number[i][j], x, y)
