#FC_Alpha_Test
#Testing for images with alpha
import pygame
from time import sleep

pygame.init()
disp = pygame.display.set_mode((400, 300), 0, 32)
img = pygame.image.load("pygame_powered_big.png").convert_alpha()
disp.fill((0,0,0))
disp.blit(img, (0,0))
disp = disp.convert_alpha()
pygame.display.flip()
sleep(1)
disp.set_alpha(20)
print(pygame.display.get_surface())
pygame.display.flip()
for i in range(256):
    img.set_alpha(i)
    print(i)
