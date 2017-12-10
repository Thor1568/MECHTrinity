#Mech Trinity
#Imported modules -------------------
import socket
from time import sleep
import pygame
import os
import sys

#Need to import everything from the libraries in config folder

g_dir = os.getcwd()
g_dir_uf = g_dir.replace("\\", "/")
cfig_dir = os.path.normpath(g_dir+"/config/ ")
#unformatted config directory
cfig_dir_uf = g_dir_uf+"/config/"
cfig_dir= cfig_dir.strip()
img_dir = os.path.normpath(g_dir+"/images/ ")
img_dir= img_dir.strip()
exec(cfig_dir_uf+"constants.py")

gameDisp = pygame.display.set_mode((disp_width, disp_height), 0, 32)
gameDisp.fill(BLACK)
