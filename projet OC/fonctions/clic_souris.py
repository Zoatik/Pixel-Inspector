import pygame
from pygame.locals import *
from fonctions.check_activity import *

def clic_souris(event):
  pos_souris_x = pygame.mouse.get_pos()[0]
  pos_souris_y = pygame.mouse.get_pos()[1]
  if event.type == MOUSEBUTTONUP:
    mouse_rect = pygame.Rect(pos_souris_x, pos_souris_y, 30, 30) #rectangle de collision du curseur
    check_activity_mouse(mouse_rect,event)
    print(pygame.mouse.get_pos())
  if event.type == MOUSEBUTTONDOWN:

    pos_souris = (pos_souris_x,pos_souris_y)
    check_pave_livre(pos_souris,event)
    check_inventory(pos_souris,event)
    
    
def move_object():
  pos_souris_x = pygame.mouse.get_pos()[0]
  pos_souris_y = pygame.mouse.get_pos()[1]
  if get_texte_se_deplace():
    pos_fausse_equation_x = get_pos_fausse_equation()[0]
    pos_fausse_equation_y = get_pos_fausse_equation()[1]
    new_pos_x = pos_souris_x - get_pos_depart()[0] + get_pos_fausse_equation()[0]
    new_pos_y = pos_souris_y - get_pos_depart()[1] + get_pos_fausse_equation()[1]
    set_pos_fausse_equation((new_pos_x,new_pos_y))
    set_pos_depart(pygame.mouse.get_pos())
  if get_inventory_se_deplace()[0]:
    new_pos_x = pos_souris_x - get_pos_depart()[0] + get_pos_key_1()[0]
    new_pos_y = pos_souris_y - get_pos_depart()[1] + get_pos_key_1()[1]
    set_pos_key_1((new_pos_x,new_pos_y))
    set_pos_depart(pygame.mouse.get_pos())
  if get_inventory_se_deplace()[1]:
    new_pos_x = pos_souris_x - get_pos_depart()[0] + get_pos_key_2()[0]
    new_pos_y = pos_souris_y - get_pos_depart()[1] + get_pos_key_2()[1]
    set_pos_key_2((new_pos_x,new_pos_y))
    set_pos_depart(pygame.mouse.get_pos())
    
    