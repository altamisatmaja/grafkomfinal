import pygame, sys
from settings import * 
from level import Level
from player import Player

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('GROUP G GRAFKOM')
clock = pygame.time.Clock()
level = Level(level_map,screen)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill('blue')
	level.run()

	pygame.display.update()
	clock.tick(60)