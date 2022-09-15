import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            small_cactus = SmallCactus(SMALL_CACTUS)
            large_cactus = LargeCactus(LARGE_CACTUS)
            bird = Bird(BIRD)
            if random.randint(0, 2) == 0:
                self.obstacles.append(small_cactus)
            elif random.randint(0, 2) == 1:
                self.obstacles.append(large_cactus)
            elif random.randint(0, 2) == 2:
                self.obstacles.append(bird)
        
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.death_count += 1
                game.playing = False
                break
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles = []
        