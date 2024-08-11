class Circle:
    pass
ens = []
def setup():
    size(600,600)
    noStroke()
    for i in range(10):
        en = Circle()
        en.radius = random(10,30)
        en.x = random(en.radius,width-en.radius)
        en.y = random(en.radius,height-en.radius)
        en.angle = random(TWO_PI)
        en.speed = random(2,6)
        en.iro = color(random(255),random(255),random(255))
        en.move = True
        ens.append(en)
def draw():
    background(255)
    for en in ens:
        if en.move:
            en.x += en.speed * cos(en.angle)
            en.y += en.speed * sin(en.angle)
            if en.x < en.radius or en.x > width-en.radius:
                en.angle = PI-en.angle
                if en.x<en.radius: en.x=en.radius
                if en.x>width-en.radius: en.x=width-en.radius
            if en.y < en.radius or en.y > height-en.radius:
                en.angle *= -1
                if en.y<en.radius: en.y=en.radius
                if en.y>height-en.radius: en.y=height-en.radius
        for other in ens:
            if en == other:
                continue
            dst = dist(en.x,en.y,other.x,other.y)
            if dst < en.radius+other.radius:
                # 接触面の法線ベクトル
                nx = (other.x-en.x)/dst
                ny = (other.y-en.y)/dst
                # 速度ベクトルを法線方向と接線方向に分解
                vn1 = en.speed*cos(en.angle)*nx+en.speed*sin(en.angle)*ny
                vn2 = other.speed*cos(other.angle)*nx+other.speed*sin(other.angle)*ny
                vt1 = -en.speed*cos(en.angle)*nx+en.speed*sin(en.angle)*ny
                vt2 = -other.speed*cos(other.angle)*nx+other.speed*sin(other.angle)*ny
                # 法線方向の速度成分の交換
                newVn1 = vn2
                newVn2 = vn1
                # 新しい速度ベクトルの再構成
                en.speed = sqrt(newVn1*newVn1 + vt1*vt1)
                other.speed = sqrt(newVn2*newVn2 + vt2*vt2)
                # 反射角度の計算
                en.angle = atan2(vt1,newVn1)
                other.angle = atan2(vt2,newVn2)
                # オーバーラップを解消するために円の位置を更新
                overlap = 0.5*(en.radius+other.radius-dst)
                en.x -= overlap*nx
                en.y -= overlap*ny
                other.x += overlap*nx
                other.y += overlap*ny
        fill(en.iro)
        ellipse(en.x,en.y,en.radius*2,en.radius*2)
