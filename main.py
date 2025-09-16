from configuration import *
from weapons import *
from sprites import *
import sys
import pygame

pygame.init()

class Spritesheet:
    def __init__(self, path):
        self.spritesheet = pygame.image.load(path).convert()
    
    def get_image(self, x,y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.spritesheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(BLACK)
        
        return sprite
class Game:
    
    def __init__(self):
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.terrain_spritesheet = Spritesheet('assets/images/terrain.png') #991,541
        self.player_spritesheet = Spritesheet('assets/images/cats.png')
        self.enemy_spritesheet = Spritesheet('assets/images/evil.png')
        self.weapon_spritesheet = Spritesheet('assets/images/sword.png')
        self.bullet_spritesheet = Spritesheet('assets/images/powerBall.png')
        self.running = True
        self.enemy_collided =False
        self.block_collided = False
        
        
        
    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j , column in enumerate(row):
                Ground(self,j,i)
                if column=='B':
                    Block(self,j,i)
                if column=='P':
                    self.player=Player(self,j,i)
                if column=="E":
                    Enemy(self,j,i)
                if column =="R":
                    Water(self,j,i)
                if column =="W":
                    Weapon(self,j,i)
    
    
    def create(self):
        self.all_sprites =pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.water =  pygame.sprite.LayeredUpdates()
        self.enemies= pygame.sprite.LayeredUpdates()
        self.mainPlayer = pygame.sprite.LayeredUpdates()
        self.weapons = pygame.sprite.LayeredUpdates()
        self.bullets = pygame.sprite.LayeredUpdates()
        self.healthbar = pygame.sprite.LayeredUpdates()
        self.createTileMap()
    
    def update(self):
        self.all_sprites.update()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
    
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    def camera(self):
        if self.enemy_collided==False and self.block_collided==False:
            pressed = pygame.key.get_pressed()
            
            if pressed[pygame.K_LEFT]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.x += PLAYER_STEPS
    
            elif pressed[pygame.K_RIGHT]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.x -= PLAYER_STEPS
                    
            elif pressed[pygame.K_UP]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.y += PLAYER_STEPS     
                    
            elif pressed[pygame.K_DOWN]:
                for i, sprite in enumerate(self.all_sprites):
                    sprite.rect.y -= PLAYER_STEPS   
                
    def main(self):
        while self.running:
            self.events()
            self.camera()
            self.update()
            self.draw()
    
    


game = Game()
game.create()
game.main()

pygame.quit()
sys.exit()
