import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (0, 0, 0)
BULLET_COLOR = (255, 0, 0)
BULLET_SPEED = 5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Bullet Example")

# Create a player character
player = pygame.Rect(400, 500, 40, 40)

# Create a list to store bullets
bullets = []
def update(bullet):
    bullet.y -= BULLET_SPEED
    screen.blit(bullet,player.centerx - 5, player.top)
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire a bullet when the spacebar is pressed
                bullet = pygame.Rect(player.centerx - 5, player.top, 10, 20)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
        player.x += 5

    # Move and draw bullets
    for bullet in bullets:
        update(bullet)
        

    # Remove bullets that have gone off-screen
    bullets = [bullet for bullet in bullets if bullet.bottom > 0]

    # Clear the screen
    screen.fill(BG_COLOR)
    
    # Draw the player character
    pygame.draw.rect(screen, (255, 255, 255), player)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(30)