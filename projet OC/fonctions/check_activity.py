import pygame
from pygame.locals import *
from pygame import mixer

from fonctions.enigme_lvl_1 import *
#from constantes import *
from fonctions.loading import *
from fonctions.gestionnaire_musique import *
from fonctions.gestionnaire_sound import *
from fonctions.ordi_is_on import *
from fonctions.afficher_texte import *
from fonctions.afficher_texte_sans_voix import *



def check_activity_mouse(position,event):#fonction qui lance un événement si les _conditions sont remplies (clic, position du perso,...)
  #cas de la souris qui clique sur un objet

  if (position.collidedict(event_rect_action_dict,1)) == ("horloge", event_rect_action_horloge) and len(get_current_problems()) == 0:#clique sur l'horloge
    probleme_horloge(position)
  if position.colliderect(livre_rect) and len(get_current_problems()) == 0:#clique sur le livre
    event_livre()
  if (position.collidedict(event_rect_action_dict,1)) == ("pilier", event_rect_action_pilier): #clique sur le pilier
    if all(get_conditions()) and is_in_inventory("full_key"): 
      play_bruitage(nom_bruitage_porte_open, 0.5, 4)
    else:
      play_bruitage(nom_bruitage_porte_closed, 0.5, 4)
  if (position.collidedict(event_rect_action_dict,1)) == ("tirelire", event_rect_action_tirelire) and len(get_current_problems()) == 0: #clique sur la tirelire (cochon)
    if not get_conditions()[1]:
      stop_all_sounds()
      play_sound(nom_voix_pix_tirelire_dire,get_volume_sound())
    elif get_conditions()[3]:
      stop_all_sounds()
      play_sound(nom_voix_pix_fascine_horloge,get_volume_sound())
    elif get_conditions()[2]:
      stop_all_sounds()
      play_sound(nom_voix_pix_remercier,get_volume_sound())
    elif get_conditions()[1]:
      stop_all_sounds()
      play_sound(nom_voix_pix_aide,get_volume_sound())
      
  if (position.collidedict(event_rect_action_dict,1)) == ("tete_robot", event_rect_action_tete_robot) and len(get_current_problems()) == 0:#clique sur la tete du robot/cadenas
    probleme_cadenas()
    
  if (position.collidedict(event_rect_action_dict,1)) == ("variable", event_rect_action_variable) and len(get_current_problems()) == 0:#clique sur l'indice concernant le code
    set_timer_afficher_texte_sans_voix()
    set_texte_sans_voix("il y a comme un nombre inscrit sur ce robot...")
  
  if (position.collidedict(event_rect_action_dict,1)) == ("ordi", event_rect_action_ordi) and len(get_current_problems()) == 0:#clique sur l'ordinateur
    i = True
    for e in get_currently_playing_sound():
      if e == (nom_sound_ordi):
        set_ordi_is_on(False)
        i = False
        #print("stop ", get_ordi_is_on())
    if i == True: 
      play_sound(nom_sound_ordi,get_volume_sound())
      #play_bruitage(nom_sound_ordi,get_volume_sound(),3)
      set_ordi_is_on(True)
      #print("joue ", get_ordi_is_on())
      
    else:
      #fadeout_bruitage(nom_sound_ordi,2,3)
      stop_sound(nom_sound_ordi)

      
  check_pave_num_click(position)
  check_pave_cadenas(position)
  check_pave_livre(position,event)
  check_inventory(position,event)
    
  
##########################################################  
def check_activity_key(position,event):
  #cas du joueur qui clique sur e
  if (position.collidedict(event_rect_action_dict,1)) == ("tirelire", event_rect_action_tirelire) and event.type == KEYDOWN: #cochon
    probleme_cochon()   

########################################################## 
def check_activity_survol(position, placement):
  if (position.collidedict(event_rect_action_dict,1)) == ("ordi", event_rect_action_ordi) and placement == 1:
    fenetre.blit(bord_ordi,(0,0))
  if (position.collidedict(event_rect_action_dict,1)) == ("tirelire", event_rect_action_tirelire) and placement == 2:
    fenetre.blit(bord_tirelire,(0,0))
  if (position.collidedict(event_rect_action_dict,1)) == ("pilier", event_rect_action_pilier) and placement == 2:
    fenetre.blit(bord_pilier,(0,0))
  if (position.collidedict(event_rect_action_dict,1)) == ("horloge", event_rect_action_horloge) and placement == 1:
    fenetre.blit(bord_horloge,(0,0))
  if (position.collidedict(event_rect_action_dict,1)) == ("lampe", event_rect_action_lampe) and placement == 1:
    fenetre.blit(lampe_on,(0,0))
  if (position.collidedict(event_rect_action_dict,1)) == ("loupe", event_rect_action_loupe) and placement == 3:
    fenetre.blit(bord_loupe,(0,0))
    

  
