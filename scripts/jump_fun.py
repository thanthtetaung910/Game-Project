import pygame
jump_sound = pygame.mixer.Sound('music/jump_sound.mp3')
def jump_sound_play():
    jump_sound.set_volume(0.1)
    jump_sound.play()

def jump_sound_fadeout():
    jump_sound.fadeout(100)