import pygame,sys,scripts.gameover2,scripts.lvl_main,scripts.vic2
from pygame.locals import*
from scripts.button import *
from scripts.lvl_main import *

#from TestEnemy import EnemyAnimation
pygame.init()
#lives class
lives=3
class Game:
    
    def __init__(self,lives):
        self.lives = lives

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over()

    def game_over(self):
        pygame.mixer.music.fadeout(100)
        #print("Game over!")
        # You can add more game over logic here if needed
        pygame.mouse.set_visible(True)
        scripts.gameover2.game_over()
        exit()

def get_font(size):
    #return pygame.font.Font("font.ttf", size)
    return pygame.font.Font("River Adventurer.ttf",size)

def run2():
    con=sqlite3.connect("mydatabase.db")
    mycursor=con.cursor()

    mycursor.execute("SELECT who FROM account Where id=1")
    result1=mycursor.fetchone()

    mycursor.execute("SELECT who FROM account Where id=2")
    result2=mycursor.fetchone()

    mycursor.execute("SELECT who FROM account Where id=3")
    result3=mycursor.fetchone()
    who1=result1[0]
    who2=result2[0]
    who3=result3[0]
    
    a=0
    star=1
    clock=pygame.time.Clock()
    pygame.mixer.pre_init( 44100, -16, 2, 512)
    pygame.mixer.set_num_channels(64)
    #pygame.display.set_caption('GUI Game Development') 

    Screen_width=1600
    Screen_height=900
    WINDOW_SIZE = ((Screen_width,Screen_height))

    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 

    display = pygame.Surface((300, 200))
    pygame.mouse.set_visible(False)
    #monitor_size = [pygame.display.Info().current_w,pygame.display.Info().current_h]

    #player_image = pygame.image.load('C:/Users/User/Desktop/project/platformer_project_9/player.png').convert()
    #player_image = pygame.image.load('C:/Users/User/Desktop/project/test_animations/idle/idle_1.png')
    #player_image.set_colorkey((255, 255, 255))

    #images
    grass_image = pygame.transform.scale(pygame.image.load('image/grass.png'),(16,16))
    dirt_image = pygame.transform.scale(pygame.image.load('image/dirt.png'),(16,16))
    brick_image = pygame.transform.scale(pygame.image.load('image/brick.png'),(16,16))
    coin_image=pygame.transform.scale(pygame.image.load('image/coin_0.png'),(12,12))
    star_image=pygame.transform.scale(pygame.image.load('image/star10.png'),(14,14))
    coin_image.set_colorkey((255,255,255))
    star_image.set_colorkey((255,255,255))
    TILE_SIZE = grass_image.get_width()

    #Sound Effects
    jump_sound = pygame.mixer.Sound('music/jump_sound.mp3')
    jump_sound.set_volume(0.1)
    
    pygame.mixer.music.load('music/theme_2.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.8)

    true_scroll = [0,0]
    def load_map(path):             #game map
        f = open(path +'.txt','r')  
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row  in data:
            game_map.append(list(row))
        return game_map
    game_map  = load_map('map3')

    global animation_frames             #player animation
    animation_frames = {}
    global animation_frame1
    animation_frame1 = {}

    def load_animation(path,frame_durations):
        global animation_frames
        global animation_frame1
        animation_name = path.split('/')[1]
        animation_frame_data = []
        n = 0
        for frame in frame_durations:
            animation_frame_id = animation_name + '_' + str(n)
            player_image = path + '/' + animation_frame_id + '.png'
            enemy_image = path + '/' + animation_frame_id + '.png '
            animation_image = pygame.image.load(player_image)
            animation_image1 = pygame.image.load(enemy_image)
            animation_image.set_colorkey((255,255,255))
            animation_image1.set_colorkey((255,255,255))
            animation_frames[animation_frame_id] = animation_image.copy()
            animation_frame1[animation_frame_id] = animation_image1.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data
    
    def change_action(action_var,frame,new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var,frame
    
    animation_database = {}
    animation_database['run'] = load_animation('test_animations/run',[7,7])
    animation_database['idle'] = load_animation('test_animations/idle',[7,7,40])
    animation_database['enemy1'] = load_animation('test_animations/enemy',[7,7,7,7,7,7,7,7,7])

    player_action = 'idle'
    choose_enemy = 'enemy1'
    player_frame = 0
    enemy_frame = 0
    player_flip = False
    enemy_flip1 = True
    enemy_flip2 = True
    enemy_flip3 = True
    enemy_flip4 = True



    def collision_test(rect, tiles):        #stay on map
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(rect, movement, tiles):        #player movement
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types
    
    def enemy_move(rect, movement, tiles):        #enemy movement
        collision_type1 = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_type1['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_type1['left'] = True
        rect.y += movement[1]
        hit_list = collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_type1['bottom'] = True
                movement[1] = movement[1]
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_type1['top'] = True
        return rect, collision_type1
    
    moving_right = False
    moving_left = False

    emove_left1 = False
    emove_right1 = True

    emove_left2 = False
    emove_right2 = True

    emove_left3 = False
    emove_right3 = True

    emove_left4 = False
    emove_right4 = True

    player_y_momentum = 0
    enemy_y_momentum1 = 0
    enemy_y_momentum2 = 0
    enemy_y_momentum3 = 0
    enemy_y_momentum4 = 0
    air_timer = 0
    rect_left=110
    rect_top=50
    map_end=2500
    player_rect = pygame.Rect(rect_left, rect_top, 16, 22)
    enemy_rect1 = pygame.Rect(280,233,22,30)
    enemy_rect2 = pygame.Rect(450,185,22,30)
    enemy_rect3 = pygame.Rect(450,233,22,30)
    enemy_rect4 = pygame.Rect(450,137,22,30)

    #treasure chest
    chest_rect = pygame.Rect(2629, 234, 25,22)
    chest_img = pygame.transform.scale((pygame.image.load('image/chest/chest_2.png')),(25,22))
    chest_img.set_colorkey((255,255,255))
    chest_img1 = pygame.transform.scale((pygame.image.load('image/chest/chest_1.png')),(25,22))
    chest_img1.set_colorkey((255,255,255))
    
    #lives image load
    game = Game(lives)
    img2 = pygame.transform.scale((pygame.image.load('image/hearts2.png')),(270,70))
    img2.set_colorkey((255,255,255))
    img3 = pygame.transform.scale((pygame.image.load('image/hearts3.png')),(270,70))   
    img3.set_colorkey((255,255,255)) 
    img4 = pygame.transform.scale((pygame.image.load('image/hearts4.png')),(270,70))
    img4.set_colorkey((255,255,255))
    img5 = pygame.transform.scale((pygame.image.load('image/hearts5.png')),(270,70))   
    img5.set_colorkey((255,255,255))   
   
    custom_event = pygame.USEREVENT + 1
    pygame.time.set_timer(custom_event, 1000)

    Running,Pause=0,1
    
    state=Running
    FONT = pygame.font.SysFont('Times New Roman', 15) 
    while True: # game loop
        display.fill((146,244,255))
        MOUSE_POS = pygame.mouse.get_pos()
        
        #player position
        true_scroll[0] += (player_rect.x-true_scroll[0]-110)/5
        true_scroll[1] += (player_rect.y-true_scroll[1]-120)/5
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        
        
        #lives action
        game.lives = game.lives
        if game.lives == 3:
            screen.blit(img2,(50,50))
        elif game.lives == 2:
            screen.blit(img3,(50,50))
        elif game.lives == 1:
            screen.blit(img4,(50,50))
        else:
            screen.blit(img5,(50,50))
        
        #pause button
        #pause_button.update(screen)


        if true_scroll[1]>=Screen_height/7:# bottom end
            game.decrease_lives()
            player_rect = pygame.Rect(rect_left, rect_top, 16, 22)

        pygame.draw.rect(display,(102,155,127),pygame.Rect(0,120,300,80))
        
        tile_rects = []
        coin_rects=[]
        star_rects=[]
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    display.blit(dirt_image, (x * TILE_SIZE - scroll[0], y * TILE_SIZE  - scroll[1]))
                if tile == '2':
                    display.blit(grass_image, (x * TILE_SIZE  - scroll[0], y * TILE_SIZE  - scroll[1]))
                if tile == '3':
                    display.blit(brick_image, (x * TILE_SIZE  - scroll[0], y * TILE_SIZE  - scroll[1]))
                if tile=='4':
                    #positions.append(((x * TILE_SIZE - scroll[0], y * TILE_SIZE  - scroll[1])))
                    
                    display.blit(coin_image, (x * TILE_SIZE  - scroll[0], y * TILE_SIZE  - scroll[1]))
                    coin_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, 12, 12))
                    
                    for coin in coin_rects:
                        if player_rect.colliderect(coin):
                            row[x]='0'
                            coin_rects.remove(coin)
                            a+=1
                if tile=='5':
                    display.blit(star_image, (x * TILE_SIZE  - scroll[0], y * TILE_SIZE  - scroll[1]))
                    star_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, 12, 12))
                        
                    for stars in star_rects:
                        if player_rect.colliderect(stars):
                            row[x]='0'
                            star_rects.remove(stars)
                            star+=1
                if tile<'4':
                    if tile != '0':
                        tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y += 1
        coin_text=FONT.render(str(a),0,"red")
        display.blit(coin_text,(270,10))
        player_movement = [0, 0]
        if moving_right:
            if true_scroll[0] >=map_end:
                true_scroll[0]=true_scroll[0]
            else:
                player_movement[0] += 1
        if moving_left:
            if true_scroll[0]<=rect_left-100:
                true_scroll[0]=true_scroll[0]
            else:
                player_movement[0] -= 1

        player_movement[1] += player_y_momentum
        player_y_momentum += 0.25
        if player_y_momentum > 4:
            player_y_momentum = 4

        if player_movement[0] == 0:
            player_action,player_frame = change_action(player_action,player_frame,'idle')
        if player_movement[0] > 0:
            player_flip = False
            player_action,player_frame = change_action(player_action,player_frame,'run')
        if player_movement[0] < 0:
            player_flip = True
            player_action,player_frame = change_action(player_action,player_frame,'run')

        player_rect, collisions = move(player_rect, player_movement, tile_rects)

        enemy_movement1 = [0,0]
        enemy_movement1[1] += 1
        
        enemy_movement2=[0,0]
        enemy_movement2[1] += 1

        enemy_movement3=[0,0]
        enemy_movement3[1] += 1

        enemy_movement4=[0,0]
        enemy_movement4[1] += 1

        if emove_left1:
            if enemy_rect1.left <= 192:
                emove_left1 = False
                emove_right1 = True  
            else:
                enemy_flip1 = True
                enemy_movement1[0] -= 1
        elif emove_right1:
            if enemy_rect1.right >= 320:
                emove_right1 = False 
                emove_left1 = True
            else:
                enemy_flip1 = False
                enemy_movement1[0] += 1

        if emove_left2:
            if enemy_rect2.left <= 337:
                emove_left2 = False
                emove_right2 = True
                
            else:
                enemy_flip2 = True
                enemy_movement2[0] -= 1
                    
        elif emove_right2:
            if enemy_rect2.right >= 620:
                emove_right2 = False 
                emove_left2 = True
                 
            else:
                enemy_flip2 = False
                enemy_movement2[0] += 1
        if emove_left3:
            if enemy_rect3.left <= 300:
                emove_left3 = False
                emove_right3 = True  
            else:
                enemy_flip3 = True
                enemy_movement3[0] -= 1
        elif emove_right3:
            if enemy_rect3.right >= 620:
                emove_right3 = False 
                emove_left3 = True
            else:
                enemy_flip3 = False
                enemy_movement3[0] += 1   
        if emove_left4:
            if enemy_rect4.left <= 337:
                emove_left4 = False
                emove_right4 = True  
            else:
                enemy_flip4 = True
                enemy_movement4[0] -= 1
        elif emove_right4:
            if enemy_rect4.right >= 620:
                emove_right4 = False 
                emove_left4 = True
            else:
                enemy_flip4 = False
                enemy_movement4[0] += 1    
        enemy_rect1, ecollisions = enemy_move(enemy_rect1, enemy_movement1, tile_rects)
        enemy_rect2, ecollisions2 = enemy_move(enemy_rect2, enemy_movement2, tile_rects)
        enemy_rect3, ecollisions3 = enemy_move(enemy_rect3, enemy_movement3, tile_rects)
        enemy_rect4, ecollisions4 = enemy_move(enemy_rect4, enemy_movement4, tile_rects)

        if ecollisions['left']:
            emove_left1=False
            emove_right1=True
        elif ecollisions['right']:
            emove_right1=False
            emove_left1=True

        if ecollisions2['left']:
            emove_left2=False
            emove_right2=True
        elif ecollisions2['right']:
            emove_right2=False
            emove_left2=True

        if ecollisions3['left']:
            emove_left3=False
            emove_right3=True
        elif ecollisions3['right']:
            emove_right3=False
            emove_left3=True
            
        if ecollisions4['left']:
            emove_left4=False
            emove_right4=True
        elif ecollisions4['right']:
            emove_right4=False
            emove_left4=True

        enemy_movement1[1] += enemy_y_momentum1
        enemy_y_momentum1 += 0.25
        if enemy_y_momentum1 > 4:
            enemy_y_momentum1 = 4

        enemy_movement2[1] += enemy_y_momentum2
        enemy_y_momentum2 += 0.25
        if enemy_y_momentum2 > 4:
            enemy_y_momentum2 = 4

        enemy_movement3[1] += enemy_y_momentum3
        enemy_y_momentum3 += 0.25
        if enemy_y_momentum3 > 4:
            enemy_y_momentum3 = 4

        enemy_movement4[1] += enemy_y_momentum4
        enemy_y_momentum4 += 0.25
        if enemy_y_momentum4 > 4:
            enemy_y_momentum4 = 4
        
        if collisions['bottom']: #air timer
            player_y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1
                
        player_frame += 1
        enemy_frame += 1
        if player_frame >= len(animation_database[player_action]):
            player_frame = 0
        if enemy_frame >= len(animation_database[choose_enemy]):
            enemy_frame = 0
        player_img_id = animation_database[player_action][player_frame]
        enemy_img_id = animation_database[choose_enemy][enemy_frame]
        player_img = animation_frames[player_img_id]
        enemy_img = animation_frame1[enemy_img_id]
        enemy_img2 = animation_frame1[enemy_img_id]
        enemy_img3 = animation_frame1[enemy_img_id]
        enemy_img4 = animation_frame1[enemy_img_id]

        #player_img_display
        display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))
        #enemies display
        display.blit(pygame.transform.flip(enemy_img,enemy_flip1,False),(enemy_rect1.x-scroll[0],enemy_rect1.y-scroll[1]))
        display.blit(pygame.transform.flip(enemy_img2,enemy_flip2,False),(enemy_rect2.x-scroll[0],enemy_rect2.y-scroll[1]))
        display.blit(pygame.transform.flip(enemy_img3,enemy_flip3,False),(enemy_rect3.x-scroll[0],enemy_rect3.y-scroll[1]))
        display.blit(pygame.transform.flip(enemy_img4,enemy_flip4,False),(enemy_rect4.x-scroll[0],enemy_rect4.y-scroll[1]))
        display.blit(chest_img,(chest_rect.x-scroll[0],chest_rect.y-scroll[1]))
        
        '''print("enemy")
        print(enemy_rect)
        print("player")
        print(player_rect)'''
        if player_rect.colliderect(enemy_rect1):
            game.decrease_lives()
            player_rect = pygame.Rect(rect_left, rect_top, 16, 22)
        if player_rect.colliderect(enemy_rect2):
            game.decrease_lives()
            player_rect = pygame.Rect(rect_left, rect_top, 16, 22)
        if player_rect.colliderect(enemy_rect3):
            game.decrease_lives()
            player_rect = pygame.Rect(rect_left, rect_top, 16, 22)
        if player_rect.colliderect(enemy_rect4):
            game.decrease_lives()
            player_rect = pygame.Rect(rect_left, rect_top, 16, 22)
        if player_rect.colliderect(chest_rect):
            display.blit(chest_img1,(chest_rect.x-scroll[0],chest_rect.y-scroll[1]))
        
        for event in pygame.event.get(): # event loop
            if event.type == QUIT: # check for window quit
                pygame.quit() # stop pygame
                sys.exit() # stop script
            if state==Running:
                pygame.mouse.set_visible(False)
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        state = Pause     #go to pause
                if event.type == custom_event:
                    if player_rect.colliderect(chest_rect):
                        val1=(a,)
                        if who1:
                            mycursor.execute("UPDATE account SET money=money+?,level=2 WHERE id=1",val1)
                            con.commit()
                        elif who2:
                            mycursor.execute("UPDATE account SET money=money+?,level=2 WHERE id=2",val1)
                            con.commit()
                        elif who3:
                            mycursor.execute("UPDATE account SET money=money+?,level=2 WHERE id=3",val1)
                            con.commit()
                        pygame.mixer.music.fadeout(100)
                        pygame.mouse.set_visible(True)
                        scripts.vic2.victory3(star)
                if event.type == KEYDOWN:      #theme music control
                    if event.key == K_m:
                        pygame.mixer.music.fadeout(100)
                        jump_sound.set_volume(0.0)
                    if event.key == K_r:
                        pygame.mixer.music.play(-1)
                        jump_sound.set_volume(0.1)
                    #movement control
                    if event.key == K_d:
                        moving_right = True
                        player_flip = False
                    if event.key == K_a:
                        moving_left = True
                        player_flip = True
                    if event.key == K_w:
                        if air_timer < 6:
                            jump_sound.play()
                            player_y_momentum = -5
                    
                if event.type == KEYUP:
                    if event.key == K_d:
                        moving_right = False
                    if event.key == K_a:
                        moving_left = False
        else:                
            if state == Pause:
                pygame.mouse.set_visible(True)
                button_img=pygame.image.load('image/Play Rect.png')
                pop_img1=pygame.transform.scale(button_img,(700,400))
                screen.blit(pop_img1,(400,250))

                MENU_TEXT1 = get_font(150).render("pause", True, "crimson")
                MENU_RECT1 = MENU_TEXT1.get_rect(center=(screen.get_width()/2, 350))
                screen.blit(MENU_TEXT1,MENU_RECT1)

                button_continue=Button(image=pygame.transform.scale(button_img,(400,80)), pos=(750, 470),text_input="Continue", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
                button_exit=Button(image=pygame.transform.scale(button_img,(400,80)), pos=(750, 570),text_input="Exit", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
                       
                for button in [button_continue, button_exit]:
                    button.changeColor(MOUSE_POS)
                    button.update(screen)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_continue.checkForInput(MOUSE_POS):
                        state=Running  
                    if button_exit.checkForInput(MOUSE_POS):
                        pygame.mixer.music.fadeout(100)
                        run_lvl_main1()
        def run_lvl_main1():
            scripts.lvl_main.main()
        pygame.display.flip()
        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        #pygame.display.update() # update display
        clock.tick(60) # maintain 60 fps  