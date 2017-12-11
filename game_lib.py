#All libraries for game will be here
#yayuz
import socket
from time import sleep
import pygame
import os
import sys
import threading


#menu_nav scripts
class menu(pygame.Surface):
    def __init__(self, width, height):
        pygame.Surface.__init__(self, size=(width, height))
        self.state = 0
        self.bg_img = pygame.image.load(img_dir+"stars1.png")
        self.play_button = Button(img_dir+"testbutton.png", (0, 0))
        self.play_button_text = self.play_button.add_text("Play", 32)
        self.instruct_button = Button(img_dir+"testbutton.png", (400, 300))
        self.buttons = pygame.sprite.LayeredUpdates()
        self.buttons.add(self.play_button, self.instruct_button)

    def instructions(self):
        pass

    def settings(self):
        pass

    def credits(self):
        pass

    def back(self):
        pass

    def star_map(self, key_input):
        pass

    def render(self, display):
        if self.state == 0:
            self.blit(self.bg_img, (0,0))
            display.blit(self, (0,0))
            self.buttons.draw(display)
            display.blit(self.play_button_text, ((self.play_button.return_pos())[0], (self.play_button.return_pos())[1]))


    def handle_mouse(self, mouse):
        #Passes mouse tuple to buttons currently drawn on menu
        sprite_list = []
        for sprite in self.buttons:
            test = sprite.ifclick(mouse)
            if test == True:
                sprite_list.append(sprite)
        return sprite_list

class Button(pygame.sprite.Sprite):
    def __init__(self, img_path, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.place = pos

    def ifclick(self, mouse):
        if mouse[0] == 1:
            if ((mouse[1] > self.rect.left) and (mouse[1] < self.rect.right)) and ((mouse[2] > self.rect.bottom) and (mouse[2] < self.rect.top)):
                return True
            else:
                return False
        else:
            return False

    def add_text(self, text, size):
        self.text = text
        self.font = pygame.font.Font("freesansbold.ttf", size)
        self.text_surf = self.font.render(self.text, False, BLACK)
        return self.text_surf
    def return_pos(self):
        return self.place

#Networking classes
#In progress networking classes
class Server:
    def __init__(self, timeout, max_users):
        socket.setdefaulttimeout(timeout)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 6573
        self.host_name = socket.gethostname()
        self.ip = socket.gethostbyname(self.host_name)
        self.sock.bind((self.ip, 6573))
        self.sock.listen(max_users)
        self.addresses = []
        self.conns = []

    def work(self):
        #Function that will be run and maintains connections between each Client and is run by thread
        while True:
            try:
                c, addr = self.sock.accept()
                self.addresses.append(addr)
                self.conns.append(c)
            except:
                pass


    def recieve(self):
        data = self.sock.recv(1024)
        data = tuple(data.decode())
        return data

    def myInfo(self):
        return (self.addresses, (self.host_name, self.ip, self.port))

    def myConns(self):
        return self.conns

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 6573
        self.host = socket.gethostname()
        #Two connection methods self.connect((ip, port)) or self.create_connection((ip, port))

    def make_conn(self, ip):
        self.ip_conn = ip
        self.sock.connect((ip, self.port))

    def myInfo(self):
        return (self.host, self.port)

    def work(self):
        #Function that maintains a connection with the server class and is controlled by thread
        pass

    def transmit(self, data):
        data = str((data, self.host))
        data = data.encode()
        self.sock.send(data)

    def recieve(self):
        data = self.sock.recv(1024)
        data = tuple(data.decode())
        return data

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

#diff is the enemy difficulty
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, diff):
        pygame.sprite.Sprite.__init__(self)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def info(self):
        #Will return a tuple to be used by the multiplayer server
        pass

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
                    tile_img = tID(gid)
                    if tile_img:
                        temp_tile = tile_sprite((x*self.tmx_map.tilewidth, y*self.tmx_map.tileheight), tile_img)
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

#Game constants
#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVY_BLUE = (0, 0, 128)
OLIVE = (128, 128,   0)
PURPLE =(128,  0, 128)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
BROWN1 = (132, 93, 51)
LGREY = (158, 158, 158)
ORANGE = (219, 118, 24)

#Game and display control
disp_width = 800
disp_height = 600
FPS = 60

#file paths
g_dir = os.getcwd()
cfig_dir = (os.path.normpath(g_dir+"/config/ ")).strip()
img_dir = (os.path.normpath(g_dir+"/images/ ")).strip()
music_dir = (os.path.normpath(g_dir+"/music/ ")).strip()
