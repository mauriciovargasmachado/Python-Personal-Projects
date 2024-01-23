import pygame
import random
import math
from pygame import mixer
import io

#FONT TRANSFORMATION
def font_bytes(font):
    with open(font,'rb')as f:
        tff_byte = f.read()
    return io.BytesIO(tff_byte)

#GAME INICIALISED
pygame.init()

#SCREEN CREATION
screen = pygame.display.set_mode((800,600))

#SCREEN ICON AND TITLE
pygame.display.set_caption('Alien Invasion')
icon = pygame.image.load('ovni.png')
pygame.display.set_icon(icon)
background = pygame.image.load('Fondo.jpg')

#SOUND EFECTS
mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)

#TEXT YOU LOSE
font_like_bytes = font_bytes('FreeSansBold.ttf')
final_font = pygame.font.Font(font_like_bytes, 32)
def final_text():
    my_final_font = final_font.render('YOU LOSE!!!', True,(255,255,255))
    screen.blit(my_final_font,(60,200))

#PLAYER VARIABLES
player_img = pygame.image.load('cohete.png')
player_x = 364
player_y = 530
position_change_x = 0
position_change_y = 0

def player(x,y):
    screen.blit(player_img,(x,y))


#ENEMY VARIABLES
enemy_img = []
enemy_x = []
enemy_y = []
enemy_change_x = []
enemy_change_y = []
enemy_amount =20

for i in range (enemy_amount):
    enemy_img.append(pygame.image.load('enemigo.png'))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(50,200))
    enemy_change_x.append(0.1)
    enemy_change_y.append(30)

def enemy(x,y,z):
    screen.blit(enemy_img[z],(x,y))


#BULLET VARIABLES
bullet_img = pygame.image.load('bala.png')
bullet_x = 0
bullet_y = player_y
bullet_change_y = 0.5
visible_bullet = False

#SCORE VARIABLES
score = 0
font_like_bytes =font_bytes('FreeSansBold.ttf')
font_type = pygame.font.Font(font_like_bytes,32)
text_x =10
text_y = 10

def show_score(x,y):
    text = font_type.render(f'Score: {score}',True,(255,255,255))
    screen.blit(text,(x,y))

def bullet(x,y):
    global visible_bullet
    visible_bullet = True
    screen.blit(bullet_img, (x+16, y+10))

#COLITION DETECTION FUNCTION

def colition(x_1,y_1,x_2,y_2):
    distance = math.sqrt(math.pow(x_1-x_2,2)+math.pow(y_2-y_1,2))
    if distance<40:
        return True
    else:
        False


#GAME LOOP
game_on = True

while game_on:

    #RBC SCREEN COLOR
    screen.blit(background,(0,0))

    #EXIT PROGRAM
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game_on = False

        #KEY DOWN EVENT LISTENER
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                print('LEFT')
                position_change_x = -0.1
            elif i.key == pygame.K_RIGHT:
                print('RIGHT')
                position_change_x = 0.1
            if i.key == pygame.K_SPACE:
                if not visible_bullet:
                    bullet_x=player_x
                    bullet(bullet_x,bullet_y)
                    print('PIU PIU!!!')
                    bullet_sound = mixer.Sound('disparo.mp3')
                    bullet_sound.play()

            if i.key == pygame.K_UP:
                print('UP')
                position_change_y = -0.1
            elif i.key == pygame.K_DOWN:
                print('DOWN')
                position_change_y = 0.1

        #KEY UP EVENT LISTENER
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                position_change_x = 0
            if i.key == pygame.K_UP or i.key == pygame.K_DOWN:
                position_change_y = 0

    show_score(text_x,text_y)



    #CHANGE IN POSITION
    player_y += position_change_y

    #KEEP INSIDE BOX Y
    if player_y <= 0:
        player_y = 0

    elif player_y >= 530:
        player_y = 530


    if player_y == 0 or player_y == 530:
        print('HIT A WALL!!!')


    player_x += position_change_x

    #KEEP INSIDE BOX X
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    if player_x == 0 or player_x == 736:
        print('HIT A WALL!!!')


    #CHANGE ENEMY POSITION
    for i in range(enemy_amount):

        #YOU LOSE
        if enemy_y[i] >500:
            for j in range (enemy_amount):
                enemy_y[j]=1000
            final_text()
            break

        enemy_x[i] += enemy_change_x[i]

    #KEEP INSIDE BOX ENEMY
        if enemy_x[i] <= 0:
            enemy_change_x[i] = 0.1
            enemy_y[i] += enemy_change_y[i]
        elif enemy_x[i] >= 736:
            enemy_change_x[i] = -0.1
            enemy_y[i] += enemy_change_y[i]

        # COLITION CALL
        hit = colition(bullet_x, bullet_y, enemy_x[i], enemy_y[i])
        if hit:
            colition_sound = mixer.Sound('Golpe_2.mp3')
            colition_sound.play()
            bullet_y = 500
            visible_bullet = False
            score += 1
            print(score)
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 200)

        enemy(enemy_x[i], enemy_y[i],i)


    #BULLET MOTION
    if bullet_y<=-64:
        bullet_y = player_y
        visible_bullet=False

    if visible_bullet:
        bullet(bullet_x,bullet_y)
        bullet_y-=bullet_change_y

    player(player_x,player_y)


    #UPDATE
    pygame.display.update()

