import pygame as pg
vec = pg.math.Vector2
from random import randint
 
enemy_image = pg.image.load("Character_Paimon_Portrait.png")
player_image = pg.image.load("Traveler_Male_Card.jpg")
arrow_image = pg.image.load("sticker_5.png")
atk_buff = pg.image.load("Enemy_Large_Pyro_Slime.png")
 
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = player_image
        self.image = pg.transform.scale(self.image, (75,150))
        self.rect = self.image.get_rect()
        self.pos = vec(100, 100)
        self.rect.center = self.pos
        self.speed = 10
        self.hp = 10
        self.ammo = 30
    
    def update(self):
        keys = pg.key.get_pressed()
 
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed
        
        if keys[pg.K_SPACE] and self.ammo >= 1:
            self.ammo -= 1
            print("shooting")
            self.projectile = Projectile(self, self.game)
        
        if self.ammo <= 1:
            self.ammo += 1
 
        print(self.ammo)
 
        self.rect.center = self.pos
        if self.rect.left < 0:
            self.rect.left = 0
 
        self.rect.center = self.pos
 


 
class Enemy(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = enemy_image
        self.image = pg.transform.scale(self.image, (175,150))
        self.rect = self.image.get_rect()
        self.pos = vec(randint(2500, 2600), randint(0, 1200)) 
        self.rect.center = self.pos
        self.speed_x = self.game.difficulty
        self.life = 50
 
        self.increase_difficulty = False
        self.difficulty_amount = 10
    
    def update(self):
        self.pos.x += self.speed_x
 
        if self.pos.x < -50:
            self.game.score -= 10
            self.kill()
 
        self.hits_o = pg.sprite.spritecollide(self, self.game.projectiles, True)

        if self.hits_o:
            self.life -= 1
        
        if self.life < 0:
            self.kill()
 
        self.rect.center = self.pos



 
class Projectile(pg.sprite.Sprite):
    def __init__(self, player, game):
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.game = game
        self.game.all_sprites.add(self)
        self.game.projectiles.add(self)
 
        self.image = arrow_image
        self.image = pg.transform.scale(self.image, (25, 25))
        self.image.set_colorkey((255,255,255))
 
        self.rect = self.image.get_rect()
        self.pos = vec(self.player.pos.x, self.player.pos.y) 
        self.rect.center = self.pos
        self.speed_x = 10
        self.damage = 1
    
    def update(self):
        self.pos.x += self.speed_x
 
        self.rect.center = self.pos
        
class Buff(pg.sprite.Sprite):
    def __init__(self,player,game):
        pg.sprite.Sprite.__init__(self)
        self.player = player
        self.game = game
        self.game.all_sprites.add(self)
        self.game.buffs.add(self)
 
        self.image = atk_buff
        self.image = pg.transform.scale(self.image, (25, 25))
        self.image.set_colorkey((255,255,255))
 
        self.rect = self.image.get_rect()
        self.pos = vec(500,500) 
        self.rect.center = self.pos
        self.speed_x = 10
        self.damage = 1
    
    def update(self):
 
        self.rect.center = self.pos