import pygame,sys
import mysql.connector
import sqlite3
import scripts.button1,scripts.gameplay,scripts.menu,scripts.gameplay1,scripts.gameplay2
from scripts.button import Button
from scripts.Tests import *

#create display window
#SCREEN_HEIGHT = 720
#SCREEN_WIDTH = 1280

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("River Adventurer.ttf", size)

def main():
	
	
	con=sqlite3.connect("mydatabase.db")
	mycursor=con.cursor()
	

	mycursor.execute("SELECT level,money,who FROM account Where id=1")
	result1=mycursor.fetchone()

	mycursor.execute("SELECT level,money,who FROM account Where id=2")
	result2=mycursor.fetchone()

	mycursor.execute("SELECT level,money,who FROM account Where id=3")
	result3=mycursor.fetchone()
	who1=result1[2]
	who2=result2[2]
	who3=result3[2]
	
	if who1:
		level=result1[0]
		money=str(result1[1])
	elif who2:
		level=result2[0]
		money=str(result2[1])
	elif who3:
		level=result3[0]
		money=str(result3[1])
	screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
	
	BG = pygame.image.load("image/bgg.jpg")
	BG1=pygame.transform.scale(BG,screen.get_size())

	#load button images
	lvl1_img = pygame.image.load('image/1.png').convert_alpha()
	lvl2_img = pygame.image.load('image/2.png').convert_alpha()
	lvl3_img = pygame.image.load('image/3.png').convert_alpha()
	coin_img=pygame.image.load('image/coin.png').convert()
	coin_img.set_colorkey((255,255,255))
	button_img=pygame.image.load('image/Play Rect.png')

	#create button instances
	lvl1_button = scripts.button1.Button(190, 315, lvl1_img, 0.8)
	lvl2_button = scripts.button1.Button(650, 585, lvl2_img, 0.8)
	lvl3_button = scripts.button1.Button(1150, 220, lvl3_img, 0.8)
	button_1=Button(image=pygame.transform.scale(button_img,(150,70)), pos=(110, 70),text_input="Back", font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
	button_2=Button(image=pygame.transform.scale(button_img,(150,70)), pos=(1400, 70),text_input=money, font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
	button_3=Button(image=pygame.transform.scale(coin_img,(80,80)), pos=(1290, 70),text_input="", font=get_font(40), base_color="#d7fcd4", hovering_color="#390225")
	
	#game loop

	while True:
		MOUSE_POS=pygame.mouse.get_pos()
		screen.blit(BG1,(0,0))
		lvl1_button.draw(screen)
		lvl2_button.draw(screen)
		lvl3_button.draw(screen)
		for button in [button_1]:
			button.changeColor(MOUSE_POS)
			button.update(screen)
		for button in [button_2,button_3]:
			button.update(screen)
		if level==1:
			if lvl1_button.check():
				scripts.gameplay.run()
		elif level==2:
			if lvl1_button.check():
				scripts.gameplay.run()
			if lvl2_button.check():				
				scripts.gameplay1.run1()
		elif level==3:
			if lvl1_button.check():
				scripts.gameplay.run()
			if lvl2_button.check():				
				scripts.gameplay1.run1()
			if lvl3_button.check():
				scripts.gameplay2.run2()	
		
		#event handlergame
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				#run = False
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if button_1.checkForInput(MOUSE_POS):
					scripts.menu.main_menu()
		pygame.display.update()
		
if __name__ == '__main__':
	main()
