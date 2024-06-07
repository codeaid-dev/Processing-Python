class Timer:
    def __init__(self,timer):
        self.timer = timer
        self.saved = 0
        self.passed = 0
    def start(self):
        if self.saved == 0:
            self.saved = millis()
    def stop(self):
        if self.saved != 0:
            self.passed = (millis()-self.saved)/1000
            self.saved = 0
        return self.passed
    def is_finished(self):
        if self.saved != 0:
            if (millis()-self.saved)/1000 >= self.timer:
                return True
            else:
                return False
        return True
    def get_time(self):
        if self.saved != 0:
            if self.is_finished():
                return self.timer
            return (millis()-self.saved)/1000
        return 0

timer=Timer(10)

def setup():
    size(300,200)

def draw():
    background(255)
    textAlign(CENTER)
    textSize(50)
    fill(255,0,0)
    if not timer.is_finished():
        text('Start',width/2,height/2)
        text(timer.get_time(),width/2,height-50)
    else:
        text('Passed Time',width/2,height/2)
        text(timer.get_time(),width/2,height-50)

def keyPressed():
    if key == ENTER:
        if timer.is_finished():
            timer.start()
        else:
            timer.stop()
