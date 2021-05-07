# import
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))

# Icon
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# caption
pygame.display.set_caption("Space")

# player
playerImg = pygame.image.load("spaceship.png")
playerX = 300
playerY = 300
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

# Enemy
enemyImg = pygame.image.load('devil.png')
enemyX = random.randint(0,536)
enemyY = 30
enemyX_change = 0.3
enemyY_change = 20

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 300
bulletY_change = 0.5
bullet_state = "ready" 

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 8, y + -8))

running = True

# Game loop
while running:
    screen.fill((155,155,155))

    # Move
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
                playerX_change = 0
                playerY_change = 0
    # Move player and bullet
    playerX += playerX_change
    playerY += playerY_change

    # bulletY += playerY_change

    # giới hạn 
    if playerX <= 0:
        playerX = 0
    if playerX >= 568:
        playerX = 568
    if playerY <= 0:
        playerY = 0
    if playerY >= 568:
        playerY = 568

    # Move enemy
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    if enemyX >= 536:
        enemyX_change = -0.3
        enemyY += enemyY_change
    if enemyY >= 200:
        enemyY = 0

    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    # Move bullet
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        
        bulletY -= bulletY_change
    
    # Xuất KQ
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

pygame.quit()