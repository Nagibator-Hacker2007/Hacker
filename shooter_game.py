
from pygame import *
from random import randint
from time import time as timer
window = display.set_mode((700,500))
display.set_caption("Gjgflb d Vthfvtcnby")
lost = 0 

bullets = sprite.Group()
num = 0
score =0
healf = 3

rel = False
class Game(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,palyer_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed = palyer_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Bennito(Game):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 65:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png",self.rect.centerx,self.rect.top,200)
        bullets.add(bullet)

class enemy(Game):
    def update(self):
        global lost
        if self.rect.y<=435:
            self.rect.y = self.rect.y + self.speed
        
        else:
            self.rect.y= -70
            self.rect.x = randint(1,70)
            lost+=1
class Bullet(Game):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:   
            
            self.kill()

Zuevas = sprite.Group()
mets = sprite.Group()
for i in range(1,5):
    Zueva = enemy("p.png",randint(1,700),0,randint(3, 7))
    Zuevas.add(Zueva)
player = Bennito("q.png",350,400,11)
Gold = Game("bullet.png",500,23,20)
background = transform.scale(image.load('galaxy.jpg'),(700,500))
game = True
finish = False
FPS = 144
font.init()
font = font.SysFont("Arial",70)
for i in range(1,5):
    healf = healf-1
    met = enemy("asteroid.png",randint(1,700),0,randint(3, 7))
    mets.add(met)    
while game :

    clock = time.Clock()
    clock.tick(FPS)
    lose1  = font.render("LOSE",1,(255,255,255))
    win1  = font.render("WIN",1,(255,255,255))
    lose  = font.render("Opu"+str(score),1,(255,255,255))
    win  = font.render("Dell"+str(score),1,(255,255,255))
    live  = font.render("Live"+str(score),1,(255,255,255))

    if not finish:
        
        if healf == 0:
            window.blit(lose1,(350,250))
            finish = True
        if score == 5:
            window.blit(win1,(359,250))
            finish = True
        if lost == 10:
            window.blit(lose1,(350,250))
            finish= True
        window.blit(background,(0,0))
        Zuevas.draw(window) 
        Zuevas.update()
        player.reset()
        Gold.reset()
        player.update()
        bullets.draw(window)
        bullets.update()
        mets.draw(window)
        mets.update()
        if rel==True:
            now = timer()
            if now-last<3:
                reload=font.render("ddddddd",1,(100,1,1))
                window.blit(reload,(20,46))
            else:
                num = 0
                rel = False 
        collide = sprite.groupcollide(Zuevas,bullets,True,True)
        coll = sprite.spritecollide(player,mets,False)
        for zu in collide :
            score = score +1
            Zueva = enemy("p.png",randint(80,1100-80),-10,randint( 1,7))
            Zuevas.add(Zueva)
    for e in event.get():
        if e.type ==QUIT:
            game= False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num<5 and rel==False:
                    player.fire()
                    num = num+1
                    if num>=5 and rel == False:
                        last = timer()
                        rel = True
    key_pressed=key.get_pressed()
    display.update()
    #time.delay(50)