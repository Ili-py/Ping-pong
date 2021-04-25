from pygame import *
from random import randint
#from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y,player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()

        if keys [K_s]and self.rect.y >0:
            self.rect.y -= self.speed

        if keys [K_w]and self.rect.y < 500:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()

        if keys [K_UP]and self.rect.y > 0:
            self.rect.y -= self.speed

        if keys [K_DOWN]and self.rect.y < 500:
            self.rect.y += self.speed

window = display.set_mode ((500,500))
window.fill((255, 250, 250))
display.set_caption('Пинг Понг')
player1 = Player('ping_pong.png',20,250,100,20,30)
player2 = Player('ping_pong.png',400,250,100,20,30)
ball = Player('tennis_ball.png',250,250,20,20,50)

game = True
finish = False

clock = time.Clock()
FPS = 60


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        
        
           

    if finish != True:
        window.fill((255, 250, 250))
        player1.update_l()
        player2.update_r()

        #ball.update()
        ball.reset() 
        player1.reset()
        player2.reset()

        display.update()
        clock.tick(FPS)