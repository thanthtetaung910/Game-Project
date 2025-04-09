import pygame,sys,scripts.lvl_main
#from Tests import *
from pygame.locals import * 

pygame.init()
def victory1(star):

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
	# set the pygame window name
	#pygame.display.set_caption('Show Text')

	# create a font object.
	# 1st parameter is the font file
	# which is present in pygame.
	# 2nd parameter is size of the font

	if star==1:
		BG = pygame.image.load("image/star1.png")
		BG.set_colorkey((255,255,255))
	elif star==2:
		BG = pygame.image.load("image/star2.png")
		BG.set_colorkey((255,255,255))
	elif star==3:
		BG = pygame.image.load("image/star3.png")
		BG.set_colorkey((255,255,255))


	BG.set_colorkey((255,255,255))
	artifact=pygame.transform.scale(pygame.image.load('image/knife.png'),(500,500))
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
		scripts.lvl_main.main()

	# infinite loop
	while True:

		
		screen.fill(blue)
		screen.blit(BG,((screen.get_width() // 2)-230, (screen.get_height() // 30)))
		screen.blit(artifact,((screen.get_width() // 2-230, (screen.get_height() // 8)*2+50)))

		
		screen.blit(text, textRect)
		screen.blit(text1, textRect1)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				run()
		pygame.display.update()

