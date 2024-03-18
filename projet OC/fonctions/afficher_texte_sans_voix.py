import pygame
from pygame import *
import time

from constantes import *
from fonctions.loading import *
from fonctions.cooldown_event import *

_text_on_write_sans_voix = False
_current_texte_sans_voix = ""
_timer_texte_sans_voix = None

def afficher_texte_sans_voix(texte,interval):
  global _text_on_write_sans_voix
  global _current_texte_sans_voix
  texte_surface = texte_font.render(texte,False,(250,250,150))
  if not cooldown_event(_timer_texte_sans_voix,interval):
    fenetre.blit(box_text, pos_box)
    fenetre.blit(texte_surface,pos_texte)
    _text_on_write_sans_voix = True
  else : 
    
    _text_on_write_sans_voix = False
    _current_texte_sans_voix = ""
def set_texte_sans_voix(texte):
  global _current_texte_sans_voix
  _current_texte_sans_voix = texte

def get_texte_sans_voix():
  global _current_texte_sans_voix
  return _current_texte_sans_voix
   
def get_afficher_texte_sans_voix():
  global _text_on_write_sans_voix
  return _text_on_write_sans_voix
  
def set_afficher_texte_sans_voix(actif):
  global _text_on_write_sans_voix
  _text_on_write_sans_voix = actif

def set_timer_afficher_texte_sans_voix():
  global _timer_texte_sans_voix
  _timer_texte_sans_voix = pygame.time.get_ticks()

