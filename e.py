# import
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600,600))

pygame.display.set_caption("SPACESHIP")

# Icon
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Space
img = pygame.image.load('spaceship.png')
playerX = 300
playerY = 300
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(img, (x, y))

# Enemy
devil = pygame.image.load('devil.png')
devilX = random.randint(0, 536)
devilY = 30
devilX_change = 0.3
devilY_change = 40

def enemy(x, y):
    screen.blit(devil, (x, y))

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 300
bulletX_change = 0
bulletY_change = 0.3
bullet_state = "ready"

def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 8, y + 8))

# Background
backgr = pygame.image.load('back.png')

# Khai báo running
running = True

# Game loop
while running:
    screen.fill((155, 155, 155))
    screen.blit(backgr, (0, 0))

    # Xử lí khi gõ phím
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # <- ; -> ; ^ ; ...
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.5
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change = -0.5
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change = 0.5
            # if event.key == pygame.K_SPACE:
            #     bullet_fire(playerX, bulletY)
        if event.type == pygame.KEYUP:
            playerX_change = 0
            playerY_change = 0

    
    playerX += playerX_change
    playerY += playerY_change

    # Giới hạn
    if playerX <= 0:
        playerX = 0
    if playerX >= 568:
        playerX = 568
    if playerY <= 0:
        playerY = 0
    if playerY >= 568:
        playerY = 568

    devilX += devilX_change
    if devilX <= 0:
        devilX_change = 0.6
        devilY += devilY_change
    elif devilX >= 536:
        devilX_change = -0.6
        devilY += devilY_change
    if devilY >= 250:
        devilY = 0
    
    if bullet_state is "fire":
        bullet_fire(playerX, bulletY)
        bulletY -= bulletY_change

    # Xuất KQ
    player(playerX,playerY)
    enemy(devilX, devilY)
    pygame.display.update()

pygame.quit()