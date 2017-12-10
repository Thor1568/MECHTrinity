#Player and npc classes
import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, img_file_tuple, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file_tuple[0])
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        #tuple that will hold all loaded images
        self.idle = 0
        self.death = 1
        self.spawn = 2
        self.reload = 3

        #Parent dictionary that will refrence subdictionaries for file locations for the animations
        self.animations_dict = {
            self.idle:pygame.image.load(img_file_tuple[0]),
            self.death:pygame.image.load(img_file_tuple[1]),
            self.spawn:pygame.image.load(img_file_tuple[2]),
            self.reload:pygame.image.load(img_file_tuple[3])
        }

    def animate(self, type):
        #Animation control that will be done by a thread
        if type == self.idle:
            #Animate idle
            self.image = self.animations_dict[self.idle]
        if type == self.death:
            #animate death
            self.image = self.animations_dict[self.death]
        if type == self.spawn:
            #spawn Animation
            self.image = self.animations_dict[self.spawn]
        if type == self.reload:
            #animate reloading
            self.image = self.animations_dict[self.reload]

    def info(self):
        #Will return a tuple to be used by the multiplayer server
        pass

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def info(self):
        #Will return a tuple to be used by the multiplayer server
        pass
