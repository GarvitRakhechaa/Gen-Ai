import pygame

pygame.mixer.init()
pygame.mixer.music.load('./output.mp3')
pygame.mixer.music.play()

# Keep the program running until audio finishes
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
