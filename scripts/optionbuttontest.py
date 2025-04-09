import pygame,sys,scripts.menu
from pygame.locals import *
from scripts.button import *

pygame.init()
# Constants
CHECKBOX_SIZE = 20
FONT = pygame.font.SysFont('Times New Roman', 40)
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("River Adventurer.ttf", size)
# Initialize the Pygame window
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)


# Main game loop
def option_main():
    BG = pygame.image.load("image/menu_bg.jpg")
    BG1=pygame.transform.scale(BG,screen.get_size())
    button_img=pygame.image.load('image/Play Rect.png')
    pop_img1=pygame.transform.scale(button_img,(320,70))

    MENU_TEXT = get_font(150).render("Artifact Adventure", True, "crimson")
    MENU_RECT = MENU_TEXT.get_rect(center=(screen.get_width()/2, 250))
    MENU_TEXT1 = get_font(150).render("Running Fighter", True, "crimson")
    MENU_RECT1 = MENU_TEXT1.get_rect(center=(screen.get_width()/2, 400))

    txt1='BACK'
    txt2='MUSIC ON'
    txt3='MUSIC OFF'
        
    back_button=Button(image=pop_img1, pos=(screen.get_width()//3, 600),text_input=txt1, font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
    music_button=Button(image=pop_img1, pos=(screen.get_width()//3*2, 600),text_input=txt2, font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")        
    #img1=pygame.transform.scale(pygame.image.load('image/heart.png'),(40,40))
    #img1.set_colorkey((255,255,255))
   
    while True:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            screen.blit(BG1, (0, 0))
	        
            MOUSE_POS=pygame.mouse.get_pos()
            for button in [back_button,music_button]:                                                                                                                                                                                       
                button.changeColor(MOUSE_POS)
                button.update(screen)

            screen.blit(MENU_TEXT,MENU_RECT)
            screen.blit(MENU_TEXT1,MENU_RECT1)

            #screen.blit(img1,(300,300))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(MOUSE_POS):
                    scripts.menu.main_menu() 
                if music_button.checkForInput(MOUSE_POS):
                    if music_button.text_input == txt2:
                        music_button=Button(image=pop_img1, pos=(screen.get_width()//3*2, 600),text_input=txt3, font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
                        pygame.mixer.music.fadeout(100)
                    elif music_button.text_input == txt3:        
                        music_button=Button(image=pop_img1, pos=(screen.get_width()//3*2, 600),text_input=txt2, font=get_font(60), base_color="#d7fcd4", hovering_color="#390225")
                        pygame.mixer.music.load('music/main_theme.mp3')
                        pygame.mixer.music.set_volume(0.5)
                        pygame.mixer.music.play(-1)
        # Update the display
        pygame.display.flip()
        
if __name__ == '__main__':
    option_main()