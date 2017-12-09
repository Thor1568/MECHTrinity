from pytmx import *
import pygame
import os
from pytmx.util_pygame import load_pygame
from time import sleep

class TileMap:
    def __init__(self, file):
        tm = load_pygame(file, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmx_map = tm

    def render(self, display, surface):
        """Renders the tilemap upon the specified surface"""
        tID = self.tmx_map.get_tile_image_by_gid
        for layer in self.tmx_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tID(gid)
                    if tile:
                        temp_tile = tile_sprite((x*self.tmx_map.tilewidth, y*self.tmx_map.tileheight), )

class tile_sprite(pygame.sprite.Sprite):
    def __init__(self, pos, tile):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(tile)
        self.rect = self.image.get_rect()
        self.place = pos
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type == tType

def main():
    temp_surf = pygame.Surface((800, 600))
    path = "C:/Users/UP2-Desk/Documents/Programming/Python/Games/Pygame_games/MECH_Trinity/config/maps/testmap.tmx"
    path = os.path.normpath(path)
    mysurf = pygame.display.set_mode((800, 600), 0, 32)
    mysurf.fill((0,0,0))
    tmx_thing = TileMap(path)
    tmx_thing.render(temp_surf, mysurf)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_UP:
                    print("UP ARROW")

if __name__ == "__main__":
    main()
