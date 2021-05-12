
import pygame
import time
import random
import math

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600)) #800,600 3360x2100 #pygame.RESIZABLE

run = True

pygame.display.set_caption("zeroKiller") #Zogolowa

icon = pygame.image.load("images/Logo.png") #PYthon.png
pygame.display.set_icon(icon)

#PLayer
playerImg = pygame.image.load("images/spaceshipp.png")
playerX = 120
playerY = 530
playerX_change = 0
playerY_change = 0

#Enemy

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemyNum = 6

for i in range(enemyNum):
    enemyImg.append(pygame.image.load("images/enemy.png"))
    enemyX.append(random.randint(0, 740))
    enemyY.append(30) #random.randint(30,150)
    enemyX_change.append(1.5)
    enemyY_change.append(20)

#Bullet
bulletImg = pygame.image.load("images/bult.png")
bulletX = 0
bulletY = 530
bulletX_change = 1.5
bulletY_change = 5
bullet_state = "Ready"

'''px = 400
py = 130'''

#Score 
scoreVal = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def showScore(x,y):
    score = font.render("Score: " + str(scoreVal), True, (170,170,170))
    screen.blit(score, (x, y))

def showDev():
    dev = pygame.font.Font('freesansbold.ttf', 25)
    devX = 600
    devY = 575
    name = dev.render("By: Calvinware", False, (170,170,170))
    screen.blit(name, (devX, devY))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False


backg = pygame.image.load("images/backg.jpg")

def music():
    pygame.mixer.music.load("Music/Allupy.mp3")
    pygame.mixer.music.play(-1)

music()

#Events

while run:

    screen.fill((0, 0, 0)) #0, 100, 255
    screen.blit(backg, (0,0)) #150,120

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change -= 2
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change += 2
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                playerY_change -= 2
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                playerY_change += 2
            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX, bulletY) #bulletY
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0 

    #player movement
    playerX += playerX_change
    #playerY += playerY_change #the player is no longer able to move in y axis

    if playerX <= 0:
        playerX = 0
    elif playerX >=740:
        playerX = 740
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 530:
        playerY = 530

    #Enemy Movement
   
    #playerY += playerY_change

    for i in range(enemyNum):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] += 1.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=740:
            enemyX_change[i] -= 1.5
            enemyY[i] += enemyY_change[i]
        elif enemyY[i] <= 0:
            enemyY[i] = 0
        elif enemyY[i] >= 530:
            enemyY[i] = 530

        #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 530
            bullet_state = "Ready"
            scoreVal += 1
            enemyX[i] = random.randint(0, 740)
            enemyY[i] = 30 #random.randint(30,150)

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY)
    

    #Bullt movemnt
    if bulletY <= 0:
        bulletY = 530
        bullet_state = "Ready"

    if bullet_state == "Fire":
        bulletX = playerX
        fire_bullet(bulletX, bulletY)
        bulletY -=  bulletY_change

    showScore(textX, textY )

    showDev()

    pygame.display.update()
