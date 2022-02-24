import pygame as pg
from waifu_sprites import *
 
WIDTH = 1920
HEIGHT = 1080 
FPS = 60
 

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
 
class Game(): 
    def __init__(self):
        pg.init()
 
        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
 
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
 
        self.new()
    
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.projectiles = pg.sprite.Group()
        self.buffs = pg.sprite.Group()
 
        self.my_player = Player(self)
        self.all_sprites.add(self.my_player)
 
        self.difficulty = -3
        self.difficulty_amount = 10
        self.increase_difficulty = False
 
        self.score = 0
 
        self.run()
 
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
 
        self.new()
 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                pg.quit()
 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    self.playing = False
                    
                            
    def update(self):
        self.all_sprites.update()
        self.hits_enemy = pg.sprite.spritecollide(self.my_player, self.enemies, True)
        if self.hits_enemy:
            self.my_player.hp -= 1
 
            if self.my_player.hp <= 0:
                self.my_player.kill()
                self.playing = False
 
        self.hits_projectile = pg.sprite.groupcollide(self.projectiles, self.enemies, False, False)
        if self.hits_projectile:
            self.score += 1
            
        self.hits_projectile = pg.sprite.spritecollide(self.my_player, self.buffs, False, False)
        if self.hits_projectile:
            self.score += 1
            
 
        while len(self.enemies) < 10:
            self.freak = Enemy(self)
            self.all_sprites.add(self.freak)
            self.enemies.add(self.freak)
 
        if self.score > self.difficulty_amount:
            self.increase_difficulty = True
 
        if self.increase_difficulty:
            self.difficulty_amount += 250
            self.increase_difficulty = False
            self.difficulty -= 1
            
        if len(self.buffs) < 1:
            self.buff = Buff(self.my_player, self)



 
    def draw(self):
        self.screen.fill(WHITE)
 
        self.all_sprites.draw(self.screen)
 
        self.text_player_hp = self.comic_sans30.render(str(self.my_player.hp), False, (RED))
        self.text_score = self.comic_sans30.render(str(self.score), False, (RED))
        
        self.screen.blit(self.text_player_hp, (10, 10))
        self.screen.blit(self.text_score, (70, 10))
 
        pg.display.update()
 
g = Game()