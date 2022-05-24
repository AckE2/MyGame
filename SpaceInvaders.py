from logging import Manager
from multiprocessing import managers
import pygame, sys
from sys import exit
from GameManager import gamemanager
from GameManager import *
from game import Game


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    
    manager = gamemanager()
    game = manager.start_game() 

    while True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            manager.save(game)
        
        if keys[pygame.K_ESCAPE]:
            manager.save(game)
            pygame.quit()
            exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill((30,30,30))
        game.run()
        
        pygame.display.flip()
        clock.tick(60)

