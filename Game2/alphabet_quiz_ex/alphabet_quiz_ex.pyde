ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
question=''
answer=''
correct=''
judge=False
startTime=0
finishTime=0
def setup():
    global question,answer,correct,startTime
    size(500,200)
    correct = ALPHABET[int(random(26))]
    for c in ALPHABET:
        if c == correct:
            continue
        question += c
    startTime = millis()

def draw():
    passedTime = millis()-startTime
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
            text('Finish Time: '+str(finishTime),width/2,height/2+50)
        else:
            text('Wrong...',width/2,height/2)
        return

    #if frameCount > 600:
    if passedTime > 10000:
        textSize(40)
        fill(255,0,0)
        text('10 seconds have passed!',width/2,height/2)

def keyPressed():
    global answer,judge,finishTime
    if judge:
        return
    if key == ENTER:
        judge = True
        finishTime = (millis()-startTime)/1000
    elif 'a'<=key<='z' or 'A'<=key<='Z':
        answer += key
