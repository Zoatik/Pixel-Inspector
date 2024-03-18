import pygame
from pygame.locals import *
from constantes import *
from fonctions.afficher_texte import *



def movement(event,pos_perso,look, moveSpeed_x, moveSpeed_y):

#################################################################joueur touche objet avec lequel il peut interragir
  if pos_perso.collidedict(event_rect_action_dict,1) == ("tirelire",event_rect_action_tirelire) :#le personnage collide avec la tirelire
    #print("appuyez sur e")
    press_e((500,595))
  else: 
    set_press_e(False)
################################################################## lance le bruitage des pas
  if (event.key == K_w or event.key == K_a or event.key == K_d or event.key == K_s) and pygame.mixer.Channel(2).get_busy() == False:
    #print("je joue les pas")
    play_bruitage(nom_bruitage_pas_marche, 1, 2)
################################################################# descendre
  if event.key == K_s:
    prev_look = look  #on stock la direction avant 
    prev_pos = pos_perso  #on stock la position avant 
    look = 1
    if pos_perso.collidelist(collisions) ==-1 : #teste la collision avec un mur
      pos_perso = pos_perso.move(0,moveSpeed_y)
      if pos_perso.collidelist(collisions) !=-1:
        look = prev_look
        pos_perso = prev_pos
    else:
      look = prev_look
      pos_perso = prev_pos
################################################################# droite
  if event.key == K_d:
    prev_look = look
    prev_pos = pos_perso
    look = 2
    if pos_perso.collidelist(collisions) ==-1:
      pos_perso = pos_perso.move(moveSpeed_x,0)
      if pos_perso.collidelist(collisions) !=-1:
        look = prev_look
        pos_perso = prev_pos
    else:
      look = prev_look
      pos_perso = prev_pos
################################################################# monter
  if event.key == K_w:
    prev_look = look
    prev_pos = pos_perso
    look = 3
    if pos_perso.collidelist(collisions) ==-1:
      pos_perso = pos_perso.move(0,-moveSpeed_y)
      if pos_perso.collidelist(collisions) !=-1:
        look = prev_look
        pos_perso = prev_pos
    else:
      look = prev_look
      pos_perso = prev_pos
################################################################# gauche
  if event.key == K_a:
    prev_pos = pos_perso 
    prev_look = look
    look = 4
    if pos_perso.collidelist(collisions) ==-1:
      pos_perso = pos_perso.move(-moveSpeed_x,0)
      if pos_perso.collidelist(collisions) !=-1:
        look = prev_look
        pos_perso = prev_pos
    else:
      look = prev_look
      pos_perso = prev_pos

  return [pos_perso,look]

