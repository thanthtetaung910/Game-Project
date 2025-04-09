import pygame,sys
class Game:
    def __init__(self):
        self.lives = 3

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over()

    def game_over(self):
        print("Game over!")
        # You can add more game over logic here if needed
        exit()


'''def main():
    game = Game()
    while game.lives > 0:
        print(f"You have {game.lives} lives left.")
        play = input("Do you want to play? (yes/no): ").lower()
        if play == "yes":
            # Replace this with your actual game logic
            print("Playing the game...")
            
            # Simulate losing a life
            game.decrease_lives()
        elif play == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    print("Thanks for playing!")'''
    
pygame.init()
time = pygame.time.Clock()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
def main():
    game = Game()
    img2 = pygame.transform.scale((pygame.image.load('image/heart2.png')),(180,50))
    img2.set_colorkey((255,255,255))
    img3 = pygame.transform.scale((pygame.image.load('image/heart3.png')),(180,50))   
    img3.set_colorkey((255,255,255)) 
    img4 = pygame.transform.scale((pygame.image.load('image/heart4.png')),(180,50))
    img4.set_colorkey((255,255,255))
    img5 = pygame.transform.scale((pygame.image.load('image/heart5.png')),(180,50))   
    img5.set_colorkey((255,255,255)) 
  
    while True:
        screen.fill((146,244,255))
        if game.lives == 3:
            screen.blit(img2,(50,50))
        elif game.lives == 2:
            screen.blit(img3,(50,50))
        elif game.lives == 1:
            screen.blit(img4,(50,50))
        else:
            screen.blit(img5,(50,50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    game.decrease_lives()
        pygame.display.update()
        time.tick(60)

if __name__ == "__main__":
    main()
