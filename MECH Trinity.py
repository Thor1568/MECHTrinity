#Mech Trinity
#Imported modules -------------------
import socket
from time import sleep
import pygame
import os
import sys

g_dir = os.getcwd()
cfig_dir = os.path.normpath(g_dir+"/config/ ")
cfig_dir= cfig_dir.strip()
img_dir = os.path.normpath(g_dir+"/images/ ")
img_dir= img_dir.strip()
exec("g_dir+/MECH_Trinity/config/constants.py")