import pygame,sys
import scripts.lvl_main,scripts.optionbuttontest,scripts.Tests,scripts.about
from pygame.locals import *
from scripts.button import Button


pygame.init()

clock=pygame.time.Clock()
#pygame.display.set_caption("Menu")
font=pygame.font.SysFont(None,20)
screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)#screen width,height,xpos,ypos
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("River Adventurer.ttf", size)
def draw_text(text,font,color,surface,x,y):#menu text
    textobj=font.render(text,1,color) #font.render to create an image (Surface) of the text,then blit this image onto another Surface
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)


def main_menu():
    while True:
        MOUSE_POS=pygame.mouse.get_pos()
        BG = pygame.image.load("image/menu_bg.jpg")
        BG1=pygame.transform.scale(BG,screen.get_size())
        screen.blit(BG1, (0, 0))

        MENU_TEXT = get_font(150).render("Artifact Adventure", True, "crimson")
        MENU_RECT = MENU_TEXT.get_rect(center=(screen.get_width()/2, 100))
        screen.blit(MENU_TEXT,MENU_RECT)

        MENU_TEXT1 = get_font(150).render("Running Fighter", True, "crimson")
        MENU_RECT1 = MENU_TEXT1.get_rect(center=(screen.get_width()/2, 250))
        screen.blit(MENU_TEXT1,MENU_RECT1)

        button_img=pygame.image.load('image/Play Rect.png')
        #button_img1=pygame.transform.scale(button_img,(250,50))
        button_1=Button(image=pygame.transform.scale(button_img,(300,70)), pos=(screen.get_width()/2, 450),text_input="Play", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
        button_2=Button(image=pygame.transform.scale(button_img,(300,70)), pos=((screen.get_width()/8*3)-50, 650),text_input="Options", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
        button_3=Button(image=pygame.transform.scale(button_img,(300,70)), pos=((screen.get_width()/8*5)+50, 650), text_input="Help", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
        button_4=Button(image=pygame.transform.scale(button_img,(300,70)), pos=((screen.get_width()/4)-100, 450), text_input="Back", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
        button_5=Button(image=pygame.transform.scale(button_img,(300,70)), pos=((screen.get_width()/4*3)+100, 450), text_input="Quit", font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")

        for button in [button_1, button_2, button_3,button_4,button_5]:
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
                    scripts.lvl_main.main()
                if button_2.checkForInput(MOUSE_POS):
                    optiontest()
                if button_3.checkForInput(MOUSE_POS):
                    game_about()
                if button_4.checkForInput(MOUSE_POS):
                    logintest()
                if button_5.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(60)
def logintest():
    scripts.Tests.login()
def optiontest():
    scripts.optionbuttontest.option_main()
def game_about():
    scripts.about.about_game()

if __name__ == '__main__':
    main_menu()
