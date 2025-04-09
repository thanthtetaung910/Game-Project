import pygame,sys,scripts.menu
from pygame.locals import *

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value for white,
# green, blue colour .
white = (255, 255, 255)
#green = (0, 255, 0)
blue = (0, 100, 128)
green = (118, 231, 206)

# assigning values to X and Y variable
X = 400
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)

# set the pygame window name
#pygame.display.set_caption('Show Text')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font

font = pygame.font.Font('River Adventurer.ttf', 32)

# create a text surface object,
# on which text is drawn on it.

text7 = font.render('Key Controls', True, 'grey')

text = font.render('W - Jump', True, 'grey')

text2 = font.render('A - Move Backward', True, 'grey') 

text3 = font.render('D - Move Forward', True, 'grey')

text4 = font.render('M  - Music Off ', True, 'grey')

text5 = font.render('Esc - Pause', True, 'grey')

text6 = font.render('R - Music On', True, 'grey')

text8 = font.render('Developed by Thant.H.A , Aung.KM , Aung.JJN , Nyein"Nu , Pyae.PM', True, 'black')



text1 = font.render('Press Any Key To Continue...', True, 'black')


# create a rectangular object for the
# text surface object
textRect = text.get_rect()
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect6=text6.get_rect()
textRect7=text7.get_rect()
textRect8=text8.get_rect()




# set the center of the rectangular object.
#textRect.center = (screen.get_width() // 2-100, (screen.get_height() // 10)*1)
#textRect1.center = (screen.get_width() // 2, (screen.get_height() // 10)*7)
'''textRect2.center = (screen.get_width() // 2-50, (screen.get_height() // 10)*2)
textRect3.center = (screen.get_width() // 2-50, (screen.get_height() // 10)*3)
textRect4.center = (screen.get_width() // 2-100, (screen.get_height() // 10)*4)
textRect6.center = (screen.get_width() // 2-100, (screen.get_height() // 10)*5)
textRect5.center = (screen.get_width() // 2, (screen.get_height() // 10)*6)'''
def run():
	scripts.menu.main_menu()
def about_game():
# infinite loop
	while True:

		# completely fill the surface object
		# with white color
		screen.fill(blue)

		# copying the text surface object
		# to the display surface object
		# at the center coordinate.
		screen.blit(text, (screen.get_width() // 4, (screen.get_height() // 16)*3))
		screen.blit(text1, (screen.get_width() // 4+500, (screen.get_height() // 16)*13))
		screen.blit(text2, (screen.get_width() // 4, (screen.get_height() // 16)*4))
		screen.blit(text3, (screen.get_width() // 4, (screen.get_height() // 16)*5))
		screen.blit(text4, (screen.get_width() // 4, (screen.get_height() // 16)*6))
		screen.blit(text5, (screen.get_width() // 4, (screen.get_height() // 16)*8))
		screen.blit(text6, (screen.get_width() // 4, (screen.get_height() // 16)*7))
		screen.blit(text7, (screen.get_width() // 4, (screen.get_height() // 16)*1))
		screen.blit(text8, (screen.get_width() // 4, (screen.get_height() // 16)*10))

		# iterate over the list of Event objects
		# that was returned by pygame.event.get() method.
		for event in pygame.event.get():

			# if event object type is QUIT
			# then quitting the pygame
			# and program both.
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				run()
				
		# Draws the surface object to the screen.
		pygame.display.update()
if __name__ == '__main__':
	about_game()
