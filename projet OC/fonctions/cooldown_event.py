import pygame
from pygame.locals import *
import time

def cooldown_event(time,cooldown):
  if pygame.time.get_ticks() - time < cooldown:
    relancer = False
  else: 
    relancer = True
    
  return relancer
  
def set_cooldown_event():
  return pygame.time.get_ticks()
  
