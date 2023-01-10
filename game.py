import pygame
import random
import math
from pygame import mixer

pygame.init()
Score_font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
# screen setup
screen = pygame.display.set_mode((960, 600))
background = pygame.image.load('universe.jpg')

# title and icon
pygame.display.set_caption("Space Invaders...")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player and its movement
player_img = pygame.image.load('player.png')
pX = 430
pY = 480
pX_change = 0

# e and its movement

enemy_range = 6
enemyImg = []
eX = []
eY = []
eX_change = []
eY_change = []
increment = 0
enemy_speed = 2

for i in range(enemy_range):
    enemyImg.append(pygame.image.load('enemy2.png'))
    eX.append(random.randint(0, 850))
    eY.append(random.randint(50, 150))
    eX_change.append(enemy_speed)
    eY_change.append(40)

enemy_range_increment = 0


def increased_enemy(num):
    global enemyImg, eX, eY, eX_change, eY_change
    for _ in range(num):
        enemyImg.append(pygame.image.load('enemy1.png'))
        eX.append(random.randint(0, 850))
        eY.append(random.randint(50, 150))
        eX_change.append(enemy_speed)
        eY_change.append(40)


# bullets
bullet_state = "ready"
bulletImg = pygame.image.load('b2.png')
bulletX = 0
bulletY = 0
bulletY_change = 10
# score and collision
score = 0


def collision(ex, bx, ey, by):
    dis = math.sqrt(math.pow((ex - bx), 2) + (math.pow((ey - by), 2)))
    return dis


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, num):
    screen.blit(enemyImg[num], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y - 40))


# game over
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


enemy_value = 0


def score_check(tim):
    global enemy_range_increment, increment, enemy_value, enemy_speed, bulletY_change
    for t in range(1, 40):
        if tim == 5 * t:
            if increment <= 5 * (t - 1):
                enemy_range_increment += 3
                enemy_value = enemy_range_increment - increment
                increased_enemy(enemy_value)
                increment = enemy_range_increment
                print(increment)
                enemy_speed += 0.5
                bulletY_change += 3


bgSound = mixer.Sound("background.wav")
bgSound.play(-1)
# main game
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX_change = -2.5
            if event.key == pygame.K_RIGHT:
                pX_change = 2.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x coordinate of the spaceship
                    bulletX = pX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pX_change = 0
            if event.key == pygame.K_SPACE:
                bullet_state = "fire"

    # player movement
    pX += pX_change
    if pX < 5:
        pX = 5
    if pX > 855:
        pX = 855

    screen.blit(player_img, (pX, pY))

    # enemy movement
    for i in range(enemy_range + enemy_range_increment):

        # Game Over
        if eY[i] > 420:
            for j in range(enemy_range):
                eY[j] = 2000
            game_over_text()
            running = False
            break

        # enemy movement
        eX[i] += eX_change[i]
        if eX[i] <= 0:
            eX_change[i] = enemy_speed
            eY[i] += eY_change[i]
        elif eX[i] >= 855:
            eX_change[i] = -enemy_speed
            eY[i] += eY_change[i]
        # collision
        distance = collision(eX[i], bulletX, eY[i], bulletY)

        if distance < 30:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bullet_state = "ready"
            # print("strike")
            bulletY = 480
            # bulletX = pX
            score += 1
            eX[i] = random.randint(0, 736)
            eY[i] = random.randint(50, 150)

            Score_text = Score_font.render("Score : " + str(score), True, (255, 255, 255))
            screen.blit(Score_text, (10, 10))
        else:
            Score_text = Score_font.render("Score : " + str(score), True, (255, 255, 255))
            screen.blit(Score_text, (10, 10))

        enemy(eX[i], eY[i], i)

    # bullet fire
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if score > 0:
        score_check(score)

    pygame.display.update()
