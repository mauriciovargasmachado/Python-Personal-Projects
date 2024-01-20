import pygame

#GAME INICIALISED
pygame.init()

#SCREEN CREATION
screen = pygame.display.set_mode((800,600))

#SCREEN ICON AND TITLE
pygame.display.set_caption('Alien Invasion')
icon = pygame.image.load('ovni.png')
pygame.display.set_icon(icon)

#PLAYER VARIABLES
player_img = pygame.image.load('cohete.png')
player_x = 364
player_y = 530
position_change_x = 0
position_change_y = 0
def player(x,y):
    screen.blit(player_img,(x,y))




#GAME LOOP
game_on = True

while game_on:

    #RBC SCREEN COLOR
    screen.fill((205,154,200))

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

    player(player_x,player_y)


    #UPDATE
    pygame.display.update()

