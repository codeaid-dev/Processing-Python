class Circle:
    def collide(self,en):
        dst = dist(self.x,self.y,en.x,en.y)
        return dst < self.size/2+en.size/2
ens = []
def setup():
    size(600,600)
    noStroke()
    for i in range(100):
        en = Circle()
        en.size = random(30,50)
        en.x = random(en.size/2,width-en.size/2)
        en.y = random(en.size/2,height-en.size/2)
        en.angle = random(360)
        en.speed = random(1,3)
        en.color = color(random(255),random(255),random(255))
        en.move = True
        ens.append(en)
def draw():
    background(0)
    for en in ens:
        if en.move:
            en.x += en.speed * cos(en.angle*PI/180)
            en.y += en.speed * sin(en.angle*PI/180)
            if en.x < en.size/2 or en.x > width-en.size/2:
                en.angle = 180-en.angle
            if en.y < en.size/2 or en.y > height-en.size/2:
                en.angle *= -1
        for other in ens:
            if en == other:
                continue
            if en.collide(other) and en.move and other.move:
                if en.size < other.size:
                    ens.remove(en)
                    other.size += en.size/5
                    if other.x < other.size/2:
                        other.x = other.size/2
                    if other.x > width-other.size/2:
                        other.x = width-other.size/2
                    if other.y < other.size/2:
                        other.y = other.size/2
                    if other.y > height-en.size/2:
                        other.y = height-en.size/2
                break
        fill(en.color)
        ellipse(en.x,en.y,en.size,en.size)
def mousePressed():
    for en in ens:
        d = dist(en.x,en.y,mouseX,mouseY)
        if d < en.size/2:
            ens.remove(en)
            for n in range(0,360,30):
                new_en = Circle()
                new_en.size = en.size/5
                new_en.x = en.x
                new_en.y = en.y
                new_en.angle = n
                new_en.speed = 1
                new_en.color = color(random(255),random(255),random(255))
                new_en.move = True
                ens.append(new_en)
            break
