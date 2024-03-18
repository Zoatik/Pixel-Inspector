import pygame
from pygame.locals import *
#from constantes import*
from fonctions.check_activity import *

def mouse_detector(placement):
  pos_souris_x = pygame.mouse.get_pos()[0]
  pos_souris_y = pygame.mouse.get_pos()[1]
  mouse_rect = pygame.Rect(pos_souris_x, pos_souris_y, 30, 30)
  check_activity_survol(mouse_rect, placement)
  
def get_mouse_rect():
  pos_souris_x = pygame.mouse.get_pos()[0]
  pos_souris_y = pygame.mouse.get_pos()[1]
  mouse_rect = pygame.Rect(pos_souris_x, pos_souris_y, 30, 30)
  return mouse_rect
