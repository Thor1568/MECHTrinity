#Mech Trinity
#Imported modules -------------------
import socket
from time import sleep
import pygame
import os
import sys
from game_lib import *

pygame.init()
gameDisp = pygame.display.set_mode((disp_height, disp_width), 0, 32)
gameDisp.fill((WHITE))
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    pygame.display.flip()
