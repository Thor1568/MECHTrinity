#Map test with my own code
from pytmx.util_pygame import load_pygame
import pytmx
import pygame
import os

g_dir = os.getcwd()
#map_dir = os.path.normpath(g_dir+"/config/maps/ ")
#map_dir= map_dir.strip()
cfig_dir = os.path.normpath(g_dir+"/config/ ")
cfig_dir= cfig_dir.strip()
#map_file = map_dir+"testmap.tmx"
map_file = pygame.image.load(cfig_dir+"testmap.png")
gameDisp = pygame.display.set_mode((800, 600), 0, 32)
gameDisp.fill((0,0,0))
#test_map = load_pygame(map_file)
#for layer in test_map.visible_layers:
#    for x, y, gid, in layer:
#        tile = test_map.get_tile_image_by_gid(gid)
#        gameDisp.blit(tile, (x * test_map.tilewidth, y * test_map.tileheight))
gameDisp.blit(map_file, (0,0))
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
        if event.type == pygame.QUIT:
            pygame.quit()
            break
print("yayuz")
