import pygame,sys,scripts.gameplay,scripts.lvl_main
from pygame.locals import *
from scripts.button import Button
from scripts.lvl_main import *

pygame.init()

clock=pygame.time.Clock()
pygame.mixer.music.load('music/main_theme.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)#screen width,height,xpos,ypos
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("River Adventurer.ttf", size)
def draw_text(text,font,color,surface,x,y):#menu text
    textobj=font.render(text,1,color) #font.render to create an image (Surface) of the text,then blit this image onto another Surface
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def game_over():
    while True:
        MOUSE_POS=pygame.mouse.get_pos()
        BG = pygame.image.load("image/bg2.png")
        BG1=pygame.transform.scale(BG,screen.get_size())
        screen.blit(BG1, (0, 0))

        
        MENU_TEXT1 = get_font(150).render("Game Over", True, "crimson")
        MENU_RECT1 = MENU_TEXT1.get_rect(center=(screen.get_width()/2, 200))
        screen.blit(MENU_TEXT1,MENU_RECT1)

        button_img=pygame.image.load('image/Play Rect.png')
        #button_img1=pygame.transform.scale(button_img,(250,50))
        button_1=Button(image=pygame.transform.scale(button_img,(300,70)), pos=(screen.get_width()/3+40, 700),text_input="Restart", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
        button_2=Button(image=pygame.transform.scale(button_img,(300,70)), pos=((screen.get_width()/3*2), 700), text_input="Exit", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
       
        for button in [button_1, button_2]:
            button.changeColor(MOUSE_POS)
            button.update(screen)

        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.checkForInput(MOUSE_POS):
                    scripts.gameplay.run()
                if button_2.checkForInput(MOUSE_POS):
                    scripts.lvl_main.main()
        pygame.display.update()
        clock.tick(60)
if __name__ == '__main__':
    game_over()
