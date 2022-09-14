import pygame
import random

from cgitb import small

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            small_cactus = SmallCactus(SMALL_CACTUS)
            large_cactus = LargeCactus(LARGE_CACTUS)
            if random.randint(0, 2) == 0:
                self.obstacles.append(small_cactus)
            elif random.randint(0, 2) == 1:
                self.obstacles.append(large_cactus)
        
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                print('Colisionó')
                pygame.time.delay(1000)
                game.playing = False
                break
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        