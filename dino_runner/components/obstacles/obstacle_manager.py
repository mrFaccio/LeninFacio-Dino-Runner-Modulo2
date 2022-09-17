import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD_TYPE, HAMMER_TYPE, DEFAULT_TYPE
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.dinosaur import Dinosaur



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
                if game.player.type != HAMMER_TYPE:
                    game.death_count += 1
                    game.playing = False
                else:
                    self.obstacles.remove(obstacle)
                    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            
    def reset_obstacles(self):
        self.obstacles = []
        
        