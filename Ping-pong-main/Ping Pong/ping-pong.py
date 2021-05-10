from pygame import *
from random import randint

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

        if keys [K_s]  and self.rect.y < 410:
            self.rect.y += self.speed

        if keys [K_w] and self.rect.y >20 : 
            self.rect.y -= self.speed
    def update_r(self):
        keys = key.get_pressed()

        if keys [K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed

        if keys [K_DOWN] and  self.rect.y < 410:
            self.rect.y += self.speed

window = display.set_mode ((500,500))
window.fill((255, 250, 250))
display.set_caption('Пинг Понг')
player1 = Player('ping_pong.png',20,250,20,100,30) 
player2 = Player('ping_pong.png',400,250,20,100,30)
ball = Player('tennis_ball.png',250,250,20,30,0)

game = True
finish = False

clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
font.init()
font1 = font.SysFont('Arial',35)
l1 = font1.render('PLAYER 1 LOSE!',True,(180,0,0))
l2 = font1.render('PLAYER 2 LOSE!',True,(180,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill((255, 250, 250))
        player1.update_l()
        player2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        ball.reset() 
        player1.reset()
        player2.reset()

        display.update()
        clock.tick(FPS)

        if ball.rect.y >=450 or ball.rect.y <= 0:
            speed_y *= -1
        if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
            speed_x *= -1
        if ball.rect.x < 1:
            finish = True
            window.blit(l1,(75,75))
        if ball.rect.x > 499:
            finish = True
            window.blit(l2,(75,75))
    display.update()
    clock.tick(FPS)
    
