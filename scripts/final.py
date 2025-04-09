import pygame,scripts.Tests
from pygame.locals import * 
pygame.init()

screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

font = pygame.font.Font("River Adventurer.ttf ",60)
text = " \n\nHe barely managed to get the three artifacts from treasure chests and save the world by setting them together."
text1 = font.render("Coming Soon ....", True, 'black') 
textRect = text1.get_rect()
textRect.center = ((screen.get_width() // 4)*3, (screen.get_height() // 10)*9)
blue=(0,100,128)
def display_text(surface, text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 1350:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height


def run():
    scripts.Tests.login()

def final_scene():
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type==pygame.KEYDOWN:
                run()
        screen.fill(blue)
        display_text(screen, text, (200,100), font, 'grey')
        screen.blit(text1,textRect)
        pygame.display.update()
if __name__ == '__main__':
    final_scene()