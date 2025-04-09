import pygame,sys,scripts.final
#from Tests import *
from pygame.locals import * 

pygame.init()
def victory3(star):

	white = (255, 255, 255)
	blue = (0, 100, 128)
	green = (118, 231, 206)

	# assigning values to X and Y variable
	X = 400
	Y = 400

	# create the display surface object
	# of specific dimension..e(X, Y).
	screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
	pygame.mixer.music.load('music/main_theme.mp3')
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(-1)

	if star==1:
		BG = pygame.image.load("image/star1.png")
		BG.set_colorkey((255,255,255))
	elif star==2:
		BG = pygame.image.load("image/star2.png")
		BG.set_colorkey((255,255,255))
	elif star==3:
		BG = pygame.image.load("image/star3.png")
		BG.set_colorkey((255,255,255))
	#BG1=pygame.transform.scale(BG,(500,500))
	artifact=pygame.transform.scale(pygame.image.load('image/shield.png'),(500,500))
	artifact.set_colorkey((255,255,255))
	font = pygame.font.Font('River Adventurer.ttf', 75)

	# create a text surface object,
	# on which text is drawn on it.
	text = font.render('V i c t o r y', True, 'yellow')
	text1 = font.render('Press Any Key To Continue...', True, 'black')

	# create a rectangular object for the
	# text surface object
	textRect = text.get_rect()
	textRect1 = text1.get_rect()

	# set the center of the rectangular object.
	textRect.center = (screen.get_width() // 2, (screen.get_height() // 8)*3-50)
	textRect1.center = (screen.get_width() // 2, (screen.get_height() // 8)*7)

	def run():
		
		scripts.final.final_scene()

	# infinite loop
	while True:
		
		

		# completely fill the surface object
		# with white color
		
		screen.fill(blue)
		screen.blit(BG,((screen.get_width() // 2)-230, (screen.get_height() // 30)))
		screen.blit(artifact,((screen.get_width() // 2-230, (screen.get_height() // 8)*2+50)))
		# copying the text surface object
		# to the display surface object
		# at the center coordinate.
		
		screen.blit(text, textRect)
		screen.blit(text1, textRect1)

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
