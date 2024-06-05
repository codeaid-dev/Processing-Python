class Bullet:
    def show(self,color):
        self.y += self.velocity
        fill(color)
        ellipse(self.x,self.y,10,10)
    def is_hit(self,ship):
        if ship.type == 'p':
            if self.x+5 > ship.x and self.x-5 < ship.x+50 \
                and self.y+5 > ship.y and self.y-5 < ship.y+10:
                return True
        if ship.type == 'e':
            dis = dist(self.x,self.y,ship.x,ship.y)
            if dis < 30:
                return True
        return False

class Ship:
    def show(self):
        fill(255)
        noStroke()
        if self.type == 'p':
            rect(self.x-25,self.y,50,10)
            rect(self.x-5,self.y-10,10,10)
        elif self.type == 'e':
            self.ufo(self.x,self.y,50)
    def shot(self):
        bullet = Bullet()
        bullet.x = self.x
        if self.type == 'p':
            bullet.y = self.y-10
            bullet.velocity = -5
        elif self.type == 'e':
            bullet.y = self.y+25
            bullet.velocity = 5
        self.bullets.append(bullet)
    def ufo(self,x,y,v):
        stroke(1)
        ellipse(x,y+v/4,v/2,v/2)
        ellipse(x-v/4,y+v/20,v/2,v/2)
        ellipse(x+v/4,y+v/20,v/2,v/2)
        ellipse(x,y,v,v/2)
        ellipse(x,y-v/4,v/4*3,v/2)

player = Ship()
enemy = Ship()
flag = False
def setup():
    size(600,800)
    player.x = width/2
    player.y = height-20
    player.type = 'p'
    player.bullets = []
    player.collision = 0
    player.crash = False
    enemy.x = width/2
    enemy.y = -25
    enemy.type = 'e'
    enemy.bullets = []
    enemy.dx = 4
    enemy.dy = 2
    enemy.collision = 0
    enemy.crash = False
def draw():
    global flag
    background(0)
    player.show()
    player.x = mouseX 
    enemy.show()
    if player.crash:
        textAlign(CENTER)
        fill(255)
        textSize(30)
        text("Lose...",300,400)
        return
    if enemy.crash:
        textAlign(CENTER)
        fill(255)
        textSize(30)
        text("Player WIN!!",300,400)
        return
        
    enemy.y += enemy.dy
    enemy.x += enemy.dx
    if enemy.x+25 > width or enemy.x-25 < 0:
        enemy.dx *= -1
    if enemy.y+25 > height:
        enemy.y = 0
    if keyPressed:
        if key == ' ' and flag==False:
            player.shot()
            flag = True 
    else:
        flag = False
    if int(random(100))%20==0:
        enemy.shot()
    if player.bullets:
        for bullet in player.bullets:
            bullet.show('#ffffff')
            if bullet.is_hit(enemy):
                player.bullets.remove(bullet)
                enemy.collision += 1
                if enemy.collision > 4:
                    enemy.crash = True
    if enemy.bullets:
        for bullet in enemy.bullets:
            bullet.show('#ff0000')
            if bullet.is_hit(player):
                enemy.bullets.remove(bullet)
                player.collision += 1
                if player.collision > 2:
                    player.crash = True
