import pygame

pygame.init()

screen = pygame.display.set_mode((500,600))

a = True

while a:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			a = False