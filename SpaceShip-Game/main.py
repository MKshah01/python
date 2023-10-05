import pygame
import sys
import random
import math
from pygame import mixer
# initialize the pygame module
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
bg_color = (0, 0, 0)


#background music
mixer.music.load('background.wav')
mixer.music.play()        #for loop we give the -1 value

# Title and logo
pygame.display.set_caption("SpaceShooting")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('playerimg.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemyimg.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Ready can't see the bullet to fire
# Fire :-bullet is currently moving
# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480  # add because fire at top of nose of ship
bulletX_change = 0
bulletY_change = 1  # movement
bullet_state = "ready"


# this function draw a image on screen by using blit method
def player(x, y):
    # screen.blit(playerImg,(playerX,playerY))
    screen.blit(playerImg, (x, y))


# Function draw the image of enemy

def enemy(x, y, i):
    # screen.blit(playerImg,(playerX,playerY))
    screen.blit(enemyImg[i], (x, y))


# function bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # x+16 means bullet is shown on the center of the screen not left


# collion of the enemy
def isCollison(enemyX, enemyY, bulletX, bulletY):
    # distance formula
    distance = math.sqrt(math.pow((enemyX - bulletX), 2) + (math.pow(enemyY - bulletY, 2)))

    if distance < 27:
        return True
    else:
        return False


# score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

#game over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("Game Over", True, (250, 250, 250))
    screen.blit(over_text,(200,250))

# game loop
running = True
while running:
    # watch keyword and mouse event
    # playerX-=0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # using keystrok and providing the movement functionality in our game

        if event.type == pygame.KEYDOWN:  # keydown method is used to check any key pressed
            # print("key is pressed")
            if event.key == pygame.K_LEFT:
                # print("left key is pressed")    #check left key press

                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                # print("right key is pressed")   #check right key press
                playerX_change = +0.3

            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX, bulletY)  # by argument playerX it follows ship move

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("key is release")  #key is relesed
                playerX_change = 0

    screen.fill(bg_color)

    playerX += playerX_change
    # set the limit of the ship not move beyond the ship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # set the movement of the enemy
    for i in range(num_of_enemies):

        #Game Over
        if enemyY[i]>420:
            for j in range(num_of_enemies):
                enemyY[j]=2000
                game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3  # set limit enemy not beyond the screen
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # collison
        collison = isCollison(enemyX[i], enemyY[i], bulletX, bulletY)
        if collison:
            sound_explosion=mixer.Sound('explosion.wav')
            sound_explosion.play()
            bulletY = 480  # reset the bullet
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 735)  # if 760 there is error  due to enemy in movement of the ship
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # movement of the bullet

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        sound_Fire = mixer.Sound('laser.wav')
        sound_Fire.play()
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)  # this is always after screen because screen need to draw first then a playery

    pygame.display.flip()
    show_score(textX, textY)
    pygame.display.update()
