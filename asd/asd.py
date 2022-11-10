import pygame, sys, random
from pygame.locals import *

pygame.init()
#main attributes
screen_height, screen_width = 900, 1800
pygame.display.set_caption('Spooky Platforms')
screen = pygame.display.set_mode([screen_width, screen_height])
bg_img = pygame.image.load('images/sky.jpg')
tiles_img = pygame.image.load('images/tower.png')
tile_2 = pygame.image.load('images/tower1.png')
right_player = pygame.image.load('images/rightFacing_player.png')
left_player = pygame.image.load('images/leftFacing_player.png')
DoubleJump_img = pygame.image.load('images/DoubleJump.png')
ShotgunRight_img = pygame.image.load('images/Shotgun_right.png')
ShotgunLeft_img = pygame.image.load('images/Shotgun_left.png')
ShotgunDown_img = pygame.image.load('images/Shotgun_down.png')
black = (0, 0, 0)

#cam
camOffsetX = 0
xpos = random.randint(300, 400)
ypos = random.randint(700, 800)
#tiles
tile1x, tile1y = 150, 700
#/tiles
'''Player'''
x,y =  tile1x + 35, tile1y - 100
vel, jump_vel1, jump_vel2 = 5, 12.5, 12.5
jump = False
falling = False
right_left = True #Determines which way the player is looking
#Abilities
DoubleJump = True
_1DoubleJump = False
Shotgun_bool = False
_1Shot = False
shot_vel = 0
shooting = False
'''/Player'''
#LEVELS
lvl1 = False
lvl2 = True
lvl3 = False
#/LEVELS

yes = False
running = True
while running:
    screen.blit(bg_img, (0, 0))
    #jump
    input_kb = pygame.key.get_pressed()
    if jump == False and input_kb[pygame.K_UP] and falling == False:
        jump = True
    if jump:
        y -= jump_vel1
        jump_vel1 -= 0.25
        if y - 100 > screen_height:
            jump = False
            jump_vel1 = jump_vel2
            x = tile1x + 35
            y = tile1y - 100
            camOffsetX = 0
    #jump
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP and jump and DoubleJump and _1DoubleJump == False:
                jump_vel1 = 12.5
                _1DoubleJump = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and Shotgun_bool and shooting == False and _1Shot == False:
                shooting = True
                shot_vel = 12.5
    #Movement
    if input_kb[pygame.K_LEFT] and x != 0 and shooting == False:
        x -= vel
        right_left = False
    if input_kb[pygame.K_RIGHT] and x + 50 != screen_width and shooting == False:
        x += vel
        right_left = True
    if right_left:
        player = screen.blit(right_player, (x, y))
    else:
        player = screen.blit(left_player, (x, y))
    #/Movement
    '''LEVEL 1'''
    if lvl1:
        if x >= (5*screen_width)/8:
             camOffsetX += 10
             x -= 10
        elif x >= (3*screen_width)/4:
             camOffsetX += 15
             x -= 15
        elif x >= (7*screen_width)/8:
             camOffsetX += 20
             x -= 20
        #tiles
        tile1 = screen.blit(tiles_img, (tile1x - camOffsetX, tile1y))
        tile2 = screen.blit(tile_2, (600 - camOffsetX, 550))
        tile3 = screen.blit(tiles_img, (1200 - camOffsetX, 700))
        tile4 = screen.blit(tile_2, (1750 - camOffsetX, 600))
        tile5 = screen.blit(tile_2, (2300- camOffsetX, 700))
        tile6 = screen.blit(tiles_img, (2800 - camOffsetX, 600))
        tile7 = screen.blit(tiles_img, (3100 - camOffsetX, 350))
        tile8 = screen.blit(tiles_img, (3600 - camOffsetX, 250))
        tile9 = screen.blit(tile_2, (4300 - camOffsetX, 600))
        tile10 = screen.blit(tiles_img, (4900 - camOffsetX, 700))
        tile11 = screen.blit(tile_2, (5400 - camOffsetX, 550))
        tile12 = screen.blit(tiles_img, (6000 - camOffsetX, 650))
        tile13 = screen.blit(tiles_img, (6650 - camOffsetX, 800))
        tile14 = screen.blit(tile_2, (7200 - camOffsetX, 600))
        tile15 = screen.blit(tiles_img, (7700 - camOffsetX, 350))
        tile16 = screen.blit(tile_2, (8300 - camOffsetX, 600))
        tile17 = screen.blit(tile_2, (8900 - camOffsetX, 750))
        tile18 = screen.blit(tiles_img, (9400 - camOffsetX, 500))
        tile19 = screen.blit(tiles_img, (10000 - camOffsetX, 650))
        tile20 = screen.blit(tile_2, (10600 - camOffsetX, 800))
        list2 = [tile1, tile2, tile3, tile4, tile5, tile6,
                 tile7, tile8, tile9, tile10, tile11, tile12,
                 tile13, tile14, tile15, tile16, tile17, tile18,
                 tile19, tile20 ]
        #collider
        index = player.collidelist(list2) 
        if index >= 0:
            jump = False
            _1DoubleJump = False
            jump_vel1=jump_vel2
            falling = False
        elif player.colliderect(tile1):
            jump = False
            _1DoubleJump = False
            jump_vel1=jump_vel2
            falling = False
        else: 
            falling = True
        if DoubleJump == False:
            doubleJump = screen.blit(DoubleJump_img, (10600 - camOffsetX, 650))
        if player.colliderect(doubleJump) and DoubleJump == False:
            DoubleJump = True
        '''if player.colliderect(list2[19]):
            lvl1 = False
            lvl2 = True
            x = tile1x + 35
            y = tile1y - 100
            camOffsetX= 0
            print("u entered lvl2")'''
        #/collider
        #gravity
        if falling and jump == False:
            y += 8
        if y - 100 > screen_height:
            x = tile1x + 35
            y = tile1y - 100
            camOffsetX = 0
        #/gravity
        #/tiles
    '''/LEVEL 1'''
    '''LEVEL 2'''
    if lvl2:
        if x >= (3*screen_width)/10:
             camOffsetX += 15
             x -= 15
        #tiles
        tile1 = screen.blit(tiles_img, (tile1x + 50 - camOffsetX, tile1y - 90))
        tile2 = screen.blit(tile_2, (1300 - camOffsetX, 800))
        tile3 = screen.blit(tiles_img, (2200 - camOffsetX, 450))
        tile4 = screen.blit(tile_2, (3200 - camOffsetX, 600))
        tile5 = screen.blit(tile_2, (3800 - camOffsetX, 700))
        tile6 = screen.blit(tile_2, (4100 - camOffsetX, 350))
        tile7 = screen.blit(tiles_img, (5000 - camOffsetX, 600))
        tile8 = screen.blit(tiles_img, (5700 - camOffsetX, 350))
        tile9 = screen.blit(tiles_img, (6800 - camOffsetX, 650))
        tile10 = screen.blit(tile_2, (7900 - camOffsetX, 500))
        tile11 = screen.blit(tile_2, (8300 - camOffsetX, 850))
        tile12 = screen.blit(tiles_img, (9000 - camOffsetX, 650))
        tile13 = screen.blit(tile_2, (9900 - camOffsetX, 500))
        tile14 = screen.blit(tiles_img, (10800 - camOffsetX, 350))
        tile15 = screen.blit(tiles_img, (11800 - camOffsetX, 700))
        tile16 = screen.blit(tile_2, (12900 - camOffsetX, 600))
        tile17 = screen.blit(tiles_img, (14000 - camOffsetX, 650))
        tile18 = screen.blit(tile_2, (15000 - camOffsetX, 750))
        tile19 = screen.blit(tile_2, (15900 - camOffsetX, 500))
        tile20 = screen.blit(tiles_img, (17000 - camOffsetX, 600))
        tile21 = screen.blit(tiles_img, (17600 - camOffsetX, 350))
        tile22 = screen.blit(tile_2, (18700 - camOffsetX, 800))
        list2 = [tile1, tile2, tile3, tile4, tile5, tile6, tile7,
                 tile8, tile9, tile10, tile11, tile12, tile13, tile14,
                 tile15, tile16, tile17, tile18, tile19, tile20, tile21, tile22]
        #collider
        index = player.collidelist(list2) 
        if index >= 0:
            jump = False
            _1DoubleJump = False
            _1Shot = False
            jump_vel1 = jump_vel2
            falling = False
        elif player.colliderect(tile1):
            jump = False
            _1DoubleJump = False
            _1Shot = False
            jump_vel1=jump_vel2
            falling = False
        else: 
            falling = True
        #shooting
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if Shotgun_bool == False:
            Shotgun = screen.blit(ShotgunRight_img, (150 - camOffsetX, 150))
        if player.colliderect(Shotgun) and Shotgun_bool == False:
            Shotgun_bool = True
        
        if Shotgun_bool and x_mouse > x:
            Shotgun = screen.blit(ShotgunRight_img, (x + 40, y + 25 ))
            right_left = True
        elif Shotgun_bool and x_mouse < x:
            Shotgun = screen.blit(ShotgunLeft_img, (x - 90, y + 25))
            right_left = False
        
        if shooting and right_left and shot_vel > 0 and _1Shot == False:
            x -= shot_vel
            y -= shot_vel + 5
            shot_vel -= 0.1
            if shot_vel <= 0:
                _1Shot = True
                shooting = False
        elif shooting and right_left == False and shot_vel > 0 and _1Shot == False:
            x += shot_vel
            y -= shot_vel + 5
            shot_vel -= 0.1
            if shot_vel <= 0:
                _1Shot = True
                shooting = False
        #shooting  
        
        '''if player.colliderect(list2[9]):
            lvl2 = False
            lvl3 = True
            x = tile1x + 75
            y = tile1y - 100
            camOffsetX= 0
            print("u entered lvl3")'''
        #/collider
        #gravity
        if falling and jump == False:
            y += 8
        if y - 100 > screen_height:
            x = tile1x + 75
            y = tile1y - 100
            camOffsetX = 0
        #/gravity
        #/tiles
    '''/LEVEL 2'''
    '''LEVEL 3
    if lvl3:
        #tiles
        tile1 = screen.blit(tiles_img, (tile1x - camOffsetX, tile1y))
        for i in range(len(list1)):
            list1[i] = screen.blit(tiles_img,( xpos + i*450 - camOffsetX, ypos))
            if i%7==0:
                xpos += 50
                ypos -= 50
            elif i%7 == 1:
                xpos -= 3
                ypos += 75
            elif i%7 ==2:
                xpos += 9
                ypos += 125
            elif i%7 == 3:
                xpos -= 1
                ypos -= 75 
            elif i%7 == 4:
                xpos += 1
                ypos *= 3/4
            elif i%7 == 5:
                xpos -= 6
                ypos += 75
            elif i%7 == 6:
                xpos += 5
                ypos -= 80
        #collider
        index = player.collidelist(list1) 
        if index >= 0:
            jump = False
            jump_vel1=jump_vel2
            falling = False
        elif player.colliderect(tile1):
            jump = False
            jump_vel1=jump_vel2
            falling = False
        else: 
            falling = True
        if player.colliderect(list1[9]):
            lvl3 = False
        #/collider
        #gravity
        if falling and jump == False:
            y += 8
        if y - 100 > screen_height:
            x = tile1x + 75
            y = tile1y - 100
            camOffsetX = 0
        #/gravity
        #/tiles
    /LEVEL 3'''
    pygame.display.update()
    pygame.time.delay(3)
pygame.quit()
sys.exit()
