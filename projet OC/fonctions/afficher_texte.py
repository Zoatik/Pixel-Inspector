import pygame
from pygame import *
import time

from constantes import *
from fonctions.gestionnaire_sound import *
from fonctions.loading import *
from fonctions.enigme_lvl_1 import *
from fonctions.cooldown_event import *

_text_on_write = False
_press_e_activation = [False,(0,0)]

def afficher_texte():
  afficher_default_texte = True
  texte_en_cours = ""
  for e in get_currently_playing_sound():
    for i in voix_texte:
      if e == i:
        texte_en_cours = voix_texte[i]
        texte_surface = texte_font.render (voix_texte[i],False,(250,250,150))
        afficher_default_texte = False
    if afficher_default_texte == True:
      texte_surface = texte_font.render (texte_lecture_en_cours,False,(250,250,150))
  fenetre.blit(box_text, pos_box)
  fenetre.blit(texte_surface,pos_texte)
  if texte_en_cours == texte_5:
    personnage_idle_anim.blit_one_frame(0,(210,25))
  else:
    cursor_anim.blit_one_frame(0,(255,51))
  
  
def set_afficher_texte():
  set_currently_playing_sound()
  global _text_on_write
  if len(get_currently_playing_sound()) == 0:
    _text_on_write = False
  else:
    _text_on_write = True
    
def get_afficher_texte():
  global _text_on_write
  return _text_on_write
  
  
def afficher_nombre_pave_numerique():
  for e in nombres_pave_surfaces:
    fenetre.blit(nombres_pave_surfaces[e],e)
    
def afficher_heure_joueur():
  i = 0
  while True:#évite modification de la liste pendant l'itération
    for e in get_heure_liste():
      if i == 0:
        fenetre.blit(timer_font.render(e,False,(165,42,42)),(362,264))
      if i == 1:
        fenetre.blit(timer_font.render(e,False,(165,42,42)),(415,264))
      if i == 2:
        fenetre.blit(timer_font.render(e,False,(165,42,42)),(541,264))
      if i == 3:
        fenetre.blit(timer_font.render(e,False,(165,42,42)),(603,264))
      i+=1
    break
    
def afficher_code_joueur():
  i = 0
  pos = [(543,400),(543,431),(543,463)]
  for e in get_code_liste():
    fenetre.blit(code_font.render(e,False,(10,42,42)),pos[i])
    i+=1
      


    
def press_e(pos):
  global _press_e_activation
  _press_e_activation[0] = True
  _press_e_activation[1] = pos
  
def set_press_e(actif):
  global _press_e_activation
  _press_e_activation[0] = actif
  
def get_press_e():
  global _press_e_activation
  return _press_e_activation

  