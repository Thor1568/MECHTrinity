from pytmx import *
import pygame
import os
from pytmx.util_pygame import load_pygame
from time import sleep

#Partially my code but some is edited from a yt video of: https://www.youtube.com/watch?v=QIXyj3WeyZM&list=PLsk-HSGFjnaGQq7ybM8Lgkh5EMxUWPm2i&index=12
#Also from https://www.youtube.com/watch?v=Mr5l4U9S4kI
class TileMap:
    def __init__(self, file_path):
        tm = load_pygame(file_path, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmx_map = tm

    def render(self):
        """Renders the tilemap upon the specified surface"""
        tID = self.tmx_map.get_tile_image_by_gid
        tiles_group = pygame.sprite.LayeredUpdates()
        for layer in self.tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tID(gid)
                    if tile:
                        temp_tile = tile_sprite((x*self.tmx_map.tilewidth, y*self.tmx_map.tileheight), tile)
                        tiles_group.add(temp_tile)

        return tiles_group

#My personal sprite class code modded for tiles
class tile_sprite(pygame.sprite.Sprite):
    def __init__(self, pos, tile):
        pygame.sprite.Sprite.__init__(self)
        self.image = tile
        self.rect = self.image.get_rect()
        self.place = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.place[0] += dx
        self.place[1] += dy

#personal test tilemap class
class myTilemap(pygame.sprite.Sprite):
    def __init__(self, file_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_pygame(file_path, pixelalpha=True)
        self.width = self.image.width * self.image.tilewidth
        self.height = self.image.height * self.image.tileheight
        self.map = self.image

    def return_img(self):
        return self.image


def main():
    path = "C:/Users/UP2-Desk/Documents/Programming/Python/Games/Pygame_games/MECH_Trinity/config/maps/testmap.tmx"
    path = os.path.normpath(path)
    mysurf = pygame.display.set_mode((800, 600), 0, 32)
    mysurf.fill((0,0,0))
    tmx_thing = TileMap(path)
    tiles_group = tmx_thing.render()
    tiles_group.draw(mysurf)
    pygame.display.flip()
#    my_map = myTilemap(path)
#    mysurf.blit(my_map.return_img(), (0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_UP:
                    print("UP ARROW")
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        mysurf.fill((0,0,0))
        tiles_group.draw(mysurf)
        pygame.display.flip()

if __name__ == "__main__":
    main()

print(tiles_group)
