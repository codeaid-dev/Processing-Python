fireworks = []

def setup():
    size(600, 600)

def draw():
    fill(0, 30)
    rect(0, 0, width, height)
    # 一定確率で新しい花火を打ち上げる
    if random(1) < 0.02:
        fireworks.append(Firework())
    # 花火を更新・描画
    for i in range(len(fireworks) - 1,-1,-1):
        f = fireworks[i]
        f.update()
        f.display()
        # 花火が終了したら削除
        if f.finished():
            fireworks.pop(i)

#--------------------------------------
# Firework
#--------------------------------------
class Firework:
    def __init__(self):
        self.x = random(100, width - 100)
        self.y = height
        self.vy = random(-11, -9)
        self.exploded = False
        self.particles = []
        # 花火の色を決める
        type = int(random(5))
        if type == 0:
            self.fireworkColor = color(255, 50, 50) # 赤
        elif type == 1:
            self.fireworkColor = color(50, 100, 255) # 青
        elif type == 2:
            self.fireworkColor = color(255, 220, 50) # 黄
        elif type == 3:
            self.fireworkColor = color(50, 255, 100) # 緑
        else:
            self.fireworkColor = color(220, 80, 255) # 紫
    
    def update(self):
        # 打ち上げ中
        if not self.exploded:
            self.y += self.vy
            # 重力
            self.vy += 0.15
            # 速度が0になったら爆発
            if self.vy >= 0:
                self.exploded = True
                # 火花を生成
                for i in range(150):
                    self.particles.append(Particle(self.x,self.y,self.fireworkColor))
        # 爆発後
        else:
            for p in self.particles:
                p.update()
    
    def display(self):
        # 打ち上げ中
        if not self.exploded:
            fill(self.fireworkColor)
            noStroke()
            ellipse(self.x, self.y, 5, 5)
        # 爆発後
        else:
            for p in self.particles:
                p.display()
    
    def finished(self):
        if not self.exploded:
            return False
        # 全粒子が消えたか確認
        for p in self.particles:
            if not p.finished():
                return False
        return True

#--------------------------------------
# Particle
#--------------------------------------
class Particle:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        angle = random(TWO_PI)
        speed = random(2, 6)
        self.vx = cos(angle) * speed
        self.vy = sin(angle) * speed
        self.life = 255
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        # 重力
        self.vy += 0.05
        # 空気抵抗
        self.vx *= 0.99
        self.vy *= 0.99
        # 徐々に消える
        self.life -= 2
    
    def display(self):
        noStroke()
        fill(self.c, self.life)
        ellipse(self.x, self.y, 4, 4)
    
    def finished(self):
        return self.life <= 0
