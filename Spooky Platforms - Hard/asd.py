import pygame, sys, random
from pygame.locals import *

pygame.init()
#main attributes
screen_height, screen_width = 900, 1800
pygame.display.set_caption('Spooky Platforms')
screen = pygame.display.set_mode([screen_width, screen_height])
Start_img = pygame.image.load('images/StartButton.png')
End_img = pygame.image.load('images/EndButton.png')
Resume_img = pygame.image.load('images/ResumeButton.png')
GoTo_img = pygame.image.load('images/GoToButton.png')
LeftArrow_img = pygame.image.load('images/LeftArrow.png')
RightArrow_img = pygame.image.load('images/RightArrow.png')
LVL1_img = pygame.image.load('images/LVL1.png')
LVL2_img = pygame.image.load('images/LVL2.png')
LVL3_img = pygame.image.load('images/LVL3.png')
WinText_img = pygame.image.load('images/WinText.png')
bg_img = pygame.image.load('images/sky.jpg')
tiles_img = pygame.image.load('images/tower.png')
tile_2 = pygame.image.load('images/tower1.png')
right_player = pygame.image.load('images/rightFacing_player.png')
left_player = pygame.image.load('images/leftFacing_player.png')
DoubleJump_img = pygame.image.load('images/DoubleJump.png')
ShotgunRight_img = pygame.image.load('images/Shotgun_right.png')
ShotgunLeft_img = pygame.image.load('images/Shotgun_left.png')
Shotgun_img = pygame.image.load('images/Shotgun_model.png')
Prize_img = pygame.image.load('images/Prize.png')
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
DoubleJump = False
_1DoubleJump = False
Shotgun_bool = False
_1Shot = False
shot_vel = 0
shooting = False
'''/Player'''
#LEVELS/Menus
StartMenu = True
WinMenu = False
EscapeMenu = False
lvlCount = 1
count = 0
StartGame = False
lvl1 = False
lvl2 = False
lvl3 = False
#/LEVELS/Menus

yes = False
running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    if StartMenu:
        x_mouse, y_mouse = pygame.mouse.get_pos()
        mouse_input = pygame.mouse.get_pressed()
        screen.fill(black)
        screen.blit(Start_img, (screen_width/2 - 150, 450))
        screen.blit(End_img, (screen_width/2 - 87.5, 700))
        if (x_mouse >= screen_width/2 - 150 and x_mouse <= screen_width/2 + 150 and
        y_mouse >= 450 and y_mouse <= 560 and mouse_input[0]):
            StartMenu = False
            StartGame = True
            lvl1 = True
        if (x_mouse >= screen_width/2 - 87.5 and x_mouse <= screen_width/2 + 87.5 and
        y_mouse >= 700 and y_mouse <= 800 and mouse_input[0]):
            running = False
    
    if EscapeMenu:
        x_mouse, y_mouse = pygame.mouse.get_pos()
        mouse_input = pygame.mouse.get_pressed()
        screen.fill(black)
        screen.blit(Resume_img, (screen_width/2 - 200, 400))
        screen.blit(GoTo_img, (screen_width/2 - 111.5, 550))
        screen.blit(End_img, (screen_width/2 - 87.5, 700))
        LeftArr = screen.blit(LeftArrow_img, (screen_width/2 + 111.5, 561))
        RightArr = screen.blit(RightArrow_img, (screen_width/2 + 437.5, 561))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if lvlCount == 1 and RightArr.collidepoint(pygame.mouse.get_pos()):
                        lvlCount += 1
                    elif lvlCount == 3 and LeftArr.collidepoint(pygame.mouse.get_pos()):
                        lvlCount -= 1
                    elif lvlCount == 2:
                        if LeftArr.collidepoint(pygame.mouse.get_pos()):
                            lvlCount -= 1
                        elif RightArr.collidepoint(pygame.mouse.get_pos()):
                            lvlCount += 1
            
        if lvlCount == 1:
            screen.blit(LVL1_img, (screen_width/2 + 187.5, 561))
        elif lvlCount == 2:
            screen.blit(LVL2_img, (screen_width/2 + 187.5, 561))
        elif lvlCount == 3:
            screen.blit(LVL3_img, (screen_width/2 + 187.5, 561))
        
        if (x_mouse >= screen_width/2 - 200 and x_mouse <= screen_width/2 + 200 and
        y_mouse >= 450 and y_mouse <= 575 and mouse_input[0]):
            StartGame = True
            EscapeMenu = False
            if lvlCount == 1:
                lvl1 = True
            elif lvlCount == 2:
                lvl2 = True
            elif lvlCount == 3:
                lvl3 = True
        if (x_mouse >= screen_width/2 - 87.5 and x_mouse <= screen_width/2 + 87.5 and
        y_mouse >= 700 and y_mouse <= 800 and mouse_input[0]):
            running = False
    if WinMenu:
        screen.fill(black)
        screen.blit(WinText_img, (screen_width/2 - 275, screen_height/2 - 225))
    if StartGame:
        screen.blit(bg_img, (0, 0))
        #jump
        input_kb = pygame.key.get_pressed()
        if jump == False and input_kb[pygame.K_UP] and falling == False:
            jump = True
        if jump:
            y -= jump_vel1
            jump_vel1 -= 0.25
            count += 1
            if y - 100 > screen_height:
                if lvl1:
                    lvl1 = False
                    lvl2 = True
                elif lvl2:
                    lvl2 = False
                    lvl3 = True
                jump = False
                jump_vel1 = jump_vel2
                x = tile1x + 35
                y = tile1y - 100
                camOffsetX = 0
        if input_kb[pygame.K_UP] and DoubleJump and jump and _1DoubleJump == False and count > 60:
                jump_vel1 = 12.5
                _1DoubleJump = True
        if pygame.mouse.get_pressed()[0] and Shotgun_bool and shooting == False and _1Shot == False:
            shooting = True
            shot_vel = 12.5
        #/jump
        '''for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Shotgun_bool:
                    if event.button == 1 and shooting == False and _1Shot == False:
                        shooting = True
                        shot_vel = 12.5'''
        
        if input_kb[pygame.K_ESCAPE]:
            EscapeMenu = True
            StartGame = False
            if lvl1:
                lvl1 = False
                lvlCount = 1
            elif lvl2:
                lvl2 = False
                lvlCount = 2
            elif lvl3:
                lvl3 = False
                lvlCount = 3

        #Movement
        if input_kb[pygame.K_LEFT] and x != 0 and shooting == False:
            x += vel
            right_left = False
        if input_kb[pygame.K_RIGHT] and x + 50 != screen_width and shooting == False:
            x -= vel
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
                count = 0
                jump_vel1=jump_vel2
                falling = False
            elif player.colliderect(tile1):
                jump = False
                _1DoubleJump = False
                count = 0
                jump_vel1=jump_vel2
                falling = False
            else: 
                falling = True
            if DoubleJump == False:
                doubleJump = screen.blit(DoubleJump_img, (10600 - camOffsetX, 650))
            if player.colliderect(doubleJump) and DoubleJump == False:
                DoubleJump = True
            #/collider
            #gravity
            if falling and jump == False:
                y += 8
            if y - 100 > screen_height:
                lvl1 = False
                lvl2 = True
                x = tile1x + 35
                y = tile1y - 100
                camOffsetX = 0
            #/gravity
            #/tiles
            '''/LEVEL 1'''
            '''LEVEL 2'''
        elif lvl2:
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
                count = 0
                _1Shot = False
                jump_vel1 = jump_vel2
                falling = False
            elif player.colliderect(tile1):
                jump = False
                _1DoubleJump = False
                count = 0
                _1Shot = False
                jump_vel1=jump_vel2
                falling = False
            else: 
                falling = True
            #shooting
            x_mouse, y_mouse = pygame.mouse.get_pos()
            if Shotgun_bool == False:
                Shotgun = screen.blit(Shotgun_img, (18700 - camOffsetX, 650))
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
            #/collider
            #gravity
            if falling and jump == False:
                y += 8
            if y - 100 > screen_height:
                lvl2 = False
                lvl3 = True
                x = tile1x + 35
                y = tile1y - 100
                camOffsetX = 0
            #/gravity
            #/tiles
            '''/LEVEL 2'''
            '''LEVEL 3'''
        elif lvl3:
            if x >= (3*screen_width)/10:
                 camOffsetX += 15
                 x -= 15
            #tiles
            tile1 = screen.blit(tiles_img, (tile1x + 50 - camOffsetX, tile1y - 90))
            tile2 = screen.blit(tile_2, (1800 - camOffsetX, 550))
            tile3 = screen.blit(tiles_img, (3500 - camOffsetX, 750))
            tile4 = screen.blit(tile_2, (5200 - camOffsetX, 800))
            tile5 = screen.blit(tile_2, (6500 - camOffsetX, 450))
            tile6 = screen.blit(tile_2, (8100 - camOffsetX, 650))
            tile7 = screen.blit(tiles_img, (9700 - camOffsetX, 700))
            list2 = [tile1, tile2, tile3, tile4, tile5, tile6, tile7]
            #collider
            index = player.collidelist(list2) 
            if index >= 0:
                jump = False
                _1DoubleJump = False
                count = 0
                _1Shot = False
                jump_vel1 = jump_vel2
                falling = False
            elif player.colliderect(tile1):
                jump = False
                _1DoubleJump = False
                count = 0
                _1Shot = False
                jump_vel1=jump_vel2
                falling = False
            else: 
                falling = True
            Prize = screen.blit(Prize_img, (9700 - camOffsetX, 350))
            if player.colliderect(Prize):
                StartGame = False
                WinMenu = True
            #shooting
            x_mouse, y_mouse = pygame.mouse.get_pos()
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
        '''/LEVEL 3'''
        pygame.time.delay(3)
    pygame.display.update()
pygame.quit()
sys.exit()
