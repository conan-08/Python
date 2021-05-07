import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))

img = pygame.image.load("d.png")
playerX = 200
playerY = 350
playerX_change = 0

def player(x, y):
    screen.blit(img, (playerX, playerY))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
    
    playerX += playerX_change

    player(playerX, playerY)
    pygame.display.update()
