import pygame
from pygame.locals import *
#from constantes import *
from fonctions.cursor_change import *
#from fonctions.loading import*
from fonctions.mouse_detector import *
#from fonctions.enigme_lvl_1 import*
from fonctions.afficher_texte import *
from fonctions.afficher_texte_sans_voix import *
from fonctions.timer_projet import *

_timer_texte = pygame.time.get_ticks()

####################################################
def creation_level(lvl):
  cursor_change(lvl)
  if lvl == 0:
    fenetre.blit(fond_accueil,(0,0)) 
    mouse_detector(3)

    
  elif lvl == 1:
    #choix_mask = cursor_2
    perso_rect = pygame.Rect(345, 615, 67, 129)
    fenetre.blit(fond,(0,0))
    fenetre.blit(horloge,(0,0))
    #fenetre.blit(personnage_idle_1,(345, 615))
    fenetre.blit(lit,(0,0))
    fenetre.blit(pilier,(0,0))
    fenetre.blit(etagere,(0,0))
    #fenetre.blit(choix_mask,(pygame.mouse.get_pos()))


######################################################
def refresh_level(lvl,perso_rect):
  pos_souris = list(pygame.mouse.get_pos())
  pos_souris[0] -= 15
  pos_souris[1] -= 15
  if lvl == 0:
    fenetre.blit(fond_accueil,(0,0))
    mouse_detector(3)

  elif lvl == 1: 
    fenetre.blit(fond,(0,0))
    fenetre.blit(horloge,(0,0))
    if get_ordi_is_on():
      ordi_on_anim.blit((0,0),0)
    else:
      ordi_off_anim.blit((0,0),0)
    if get_conditions()[4] == True:
      fenetre.blit(tete_robot, (0,0))
    mouse_detector(1)#permet de mettre en surbrillance un objet //(1) = background
    personnage_idle_anim.blit(perso_rect, 0)
    fenetre.blit(lit,(0,0))
    fenetre.blit(pilier,(0,0))
    fenetre.blit(etagere,(0,0))
    mouse_detector(2)#(2) = foreground
    if get_press_e()[0]:#se lance quand le personnage principal peut intéragir avec le décor
      fenetre.blit(press_e,get_press_e()[1])
    for item in get_inventory():#regarde quels objets il faut afficher à l'écran
      if item == "frag_clef_1":
        fenetre.blit(frag_key_1_lvl_1,get_pos_key_1())
      if item == "outil_horloge":
        fenetre.blit(outil_horloge,(10,10))
      if item == "frag_clef_2":
        fenetre.blit(frag_key_2_lvl_1,get_pos_key_2())
      if item == "full_key":
        fenetre.blit(full_key_lvl_1,(10,10))

    for problem in get_current_problems():
      if problem == "horloge":
        fenetre.blit(fond_censored,(0,0))
        fenetre.blit(pave_numerique,(324,232))
        afficher_nombre_pave_numerique()
        afficher_heure_joueur()
      if problem == "cadenas":
        fenetre.blit(fond_censored,(0,0))
        if get_conditions()[4] == False:
          fenetre.blit(cadenas_closed,(324,232))
          fenetre.blit(cadenas_button,(579,400))
          fenetre.blit(cadenas_button,(579,433))
          fenetre.blit(cadenas_button,(579,466))
        else:
          fenetre.blit(cadenas_open,(324,232))
        fenetre.blit(quit_button,(494,517))
        afficher_code_joueur()
      if problem == "livre":
        fenetre.blit(fond_censored,(0,0))
        fenetre.blit(livre,(255,200))
        fenetre.blit(vraie_equation,(255,200))
        fenetre.blit(texte_ennui,(515,289))
        fenetre.blit(fausse_equation,get_pos_fausse_equation())
        fenetre.blit(quit_button,(758,244))
    set_afficher_texte()#permet de mettre a jour si l'affichage de la box + texte doit ou non s'effectuer
    if get_afficher_texte():
      afficher_texte()#affiche le texte en lien avec les voix
    if len(get_texte_sans_voix()) != 0 and get_afficher_texte() == False:
      global _timer_texte
      afficher_texte_sans_voix(get_texte_sans_voix(),3000)#affiche un texte sans voix
    cursor_anim.blit((pos_souris), 0)
    fenetre.blit(chronometre,(820,10))


