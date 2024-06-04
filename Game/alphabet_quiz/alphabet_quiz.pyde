ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
question=''
answer=''
correct=''
judge=False
def setup():
    global question,answer,correct
    size(500,200)
    correct = ALPHABET[int(random(26))]
    for c in ALPHABET:
        if c == correct:
            continue
        question += c

def draw():
    background(255)
    textAlign(CENTER)
    textSize(30)
    fill(0)
    text(question,width/2,50)
    noFill()
    rect(200,95,100,60)
    fill(0,255,0)
    text(answer,width/2,145)
    if judge:
        textSize(50)
        fill(255,0,0)
        if answer.upper() == correct:
            text('Correct!',width/2,height/2)
        else:
            text('Wrong...',width/2,height/2)

def keyPressed():
    global answer,judge
    if judge:
        return
    if key == ENTER:
        judge = True
    elif 'a'<=key<='z' or 'A'<=key<='Z':
        answer += key
