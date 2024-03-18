import pygame 
from pygame.locals import *
import time
from fonctions.inventory import *
from constantes import *
from fonctions.afficher_texte_sans_voix import *
from fonctions.gestionnaire_sound import*


conditions = [True,False,False,False,False] #conditions de départ et il faudra qu'elles passent toutes à True pour la fin du level
_current_problems = []
_heure_liste = []
_reponse_probleme_cadenas = ["1","1","8"]
_fausse_reponse_probleme_cadenas = ["1","1","9"]
_liste_code_cadenas = ["0","0","0"]
_pos_fausse_equation = (280,293)
_pos_x = _pos_fausse_equation[0]
_pos_y = _pos_fausse_equation[1]
_pos_depart = None
_rect_fausse_equation = pygame.Rect(_pos_x,_pos_y,215,142)
_texte_se_deplace = False #permet de savoir quand bouger le faux texte pour l'énigme du cadenas
_frag_key_1_se_deplace = False
_frag_key_2_se_deplace = False
_pos_key_1 = (10,10)
_pos_key_2 = (100,10)
_rect_key_1 = pygame.Rect(10,10,80,79)
_rect_key_2 = pygame.Rect(100,10,80,79)


def get_conditions():
  global conditions
  return conditions

def get_current_enigme_lvl_1():
  global _pos_fausse_equation
  global _pos_depart
  global _rect_fausse_equation
  global _texte_se_deplace
  global conditions
  global _current_problems
  global _heure_liste
  global _reponse_probleme_cadenas
  global _fausse_reponse_probleme_cadenas
  global _liste_code_cadenas
  global _pos_x
  global _pos_y
  global _frag_key_1_se_deplace
  global _frag_key_2_se_deplace
  global _rect_key_1
  global _rect_key_2
  global _pos_key_1
  global _pos_key_2 
  
  list_sauvegarde_enigme_lvl_1 = [
  conditions,".",
  _current_problems,".",
  _heure_liste,".",
  _reponse_probleme_cadenas,".",
  _fausse_reponse_probleme_cadenas,".",
  _liste_code_cadenas,".",
  _pos_fausse_equation,".",
  _pos_x,".",
  _pos_y,".",
  _pos_depart,".",
  _rect_fausse_equation,".",
  _texte_se_deplace,".",
  _frag_key_1_se_deplace,".",
  _frag_key_2_se_deplace,".",
  _rect_key_1,".",
  _rect_key_2,".",
  _pos_key_1,".",
  _pos_key_2]
  
  return list_sauvegarde_enigme_lvl_1

def reset_enigme_lvl_1():
  global _pos_fausse_equation
  global _pos_depart
  global _rect_fausse_equation
  global _texte_se_deplace
  global conditions
  global _current_problems
  global _heure_liste
  global _reponse_probleme_cadenas
  global _fausse_reponse_probleme_cadenas
  global _liste_code_cadenas
  global _pos_x
  global _pos_y
  global _frag_key_1_se_deplace
  global _frag_key_2_se_deplace
  global _rect_key_1
  global _rect_key_2
  global _pos_key_1
  global _pos_key_2 
  conditions = [True,False,False,False,False]
  _current_problems = []
  _heure_liste = []
  _reponse_probleme_cadenas = ["1","1","8"]
  _fausse_reponse_probleme_cadenas = ["1","1","9"]
  _liste_code_cadenas = ["0","0","0"]
  _pos_fausse_equation = (280,293)
  _pos_x = _pos_fausse_equation[0]
  _pos_y = _pos_fausse_equation[1]
  _pos_depart = None
  _rect_fausse_equation = pygame.Rect(_pos_x,_pos_y,215,142)
  _texte_se_deplace = False
  _frag_key_1_se_deplace = False
  _frag_key_2_se_deplace = False
  _rect_key_1 = pygame.Rect(10,10,80,79)
  _rect_key_2 = pygame.Rect(10,100,80,79)
  _pos_key_1 = (10,10)
  _pos_key_2 = (100,10)

######################################################fonctions gestion des problemes
def add_current_problem(nom_probleme):
  global _current_problems
  _current_problems.append(nom_probleme)
  
def remove_current_problem(nom_probleme):
  global _current_problems
  if len(_current_problems) != 0:
    _current_problems.remove(nom_probleme)

def get_current_problems():
  global _current_problems
  return _current_problems
  
#######################################################fonctions problemes à lancer
def probleme_horloge(position):

  if not conditions[1]:
    set_timer_afficher_texte_sans_voix()
    set_texte_sans_voix("L'horloge est cassée.")
       
  elif not conditions[2]:

    add_current_problem("horloge")

  else:
    set_timer_afficher_texte_sans_voix()
    set_texte_sans_voix("l'horloge indique "+time.strftime("%H:%M"))


def probleme_cochon():
       
  if not conditions[1]:
               
    give_item("outil_horloge")
    play_sound(nom_voix_tirelire_enfin_qqun,1)            
    conditions[1] = True 
  elif not conditions[2] and conditions[1]:
    play_sound(nom_voix_tirelire_pas_le_time,1) 
  if conditions[3]:
    play_sound(nom_voix_tirelire_si_tu_te_poses_la_question,1) 
  if conditions[2] and not conditions[3]:
    play_sound(nom_voix_tirelire_remercier,1)           
    conditions[3]=True #la condition 3 symbolise le premier morceau de la clef
    give_item("frag_clef_1")
     
def probleme_cadenas():
       
  if not  conditions[4]:
    add_current_problem("cadenas")

     
def event_livre():#livre avec l'indice/équation pour le cadeanas 
  add_current_problem("livre") 

##############################################################fonctions horloge
def get_heure_liste():
  return _heure_liste

def compare_heure():
  global _heure_liste
  reponse_probleme_horloge=list(time.strftime("%H%M"))
  print("reponse: ",reponse_probleme_horloge)
  print("donné: ", _heure_liste)
  if reponse_probleme_horloge == _heure_liste:
    remove_current_problem('horloge')
    set_timer_afficher_texte_sans_voix()
    set_texte_sans_voix("vous avez remis l'horloge à "+time.strftime("%H:%M"))
    print("vous avez remis l'horloge à "+time.strftime("%H:%M"))
    conditions[2]=True
    remove_inventory_item("outil_horloge")
  else:
    _heure_liste.clear()
    stop_all_sounds()
    play_sound(nom_voix_inspecteur_pas_fonctionner,1)
    print("ça n'a pas l'air de fonctionner...")
   
def add_heure_joueur(nombre):
  global _heure_liste
  if len(_heure_liste)< 4:
    _heure_liste += str(nombre)
  #print(nombre)
  
def remove_heure_joueur():
  global _heure_liste
  if len(_heure_liste) > 0:
    _heure_liste.pop()
  
def check_pave_num_click(position):
  for e in get_current_problems():
    if e == "horloge":
      if (position.collidelist(pave_num_rects)) == 0 :#clique sur un nombre du pavé numérique 
        add_heure_joueur(0)
        #return False
      if (position.collidelist(pave_num_rects)) == 1 :#clique sur un nombre du pavé numérique 
        add_heure_joueur(1)
        #return False
      if (position.collidelist(pave_num_rects)) == 2 :#clique sur un nombre du pavé numérique 
        add_heure_joueur(2)
        #return False
      if (position.collidelist(pave_num_rects)) == 3 :#clique sur un nombre du pavé numérique
        add_heure_joueur(3)
        #return False
      if (position.collidelist(pave_num_rects)) == 4 :#clique sur un nombre du pavé numérique 
        add_heure_joueur(4)
        #return False
      if (position.collidelist(pave_num_rects)) == 5 :#clique sur un nombre du pavé numérique 
        add_heure_joueur(5)
        #return False
      if (position.collidelist(pave_num_rects)) == 6 :#clique sur un nombre du pavé numérique
        add_heure_joueur(6)
        #return False
      if (position.collidelist(pave_num_rects)) == 7 :#clique sur un nombre du pavé numérique
        add_heure_joueur(7)
        #return False
      if (position.collidelist(pave_num_rects)) == 8 :#clique sur un nombre du pavé numérique 
        add_heure_joueur(8)
        #return False
      if (position.collidelist(pave_num_rects)) == 9 :#clique sur un nombre du pavé numérique 
        add_heure_joueur(9)
        #return False
      if (position.collidelist(pave_num_rects)) == 10 :#clique sur un nombre du pavé numérique : supprime
        remove_heure_joueur()
        #return False
      if (position.collidelist(pave_num_rects)) == 11 :#clique sur un nombre du pavé numérique : entrer
        compare_heure()
        #return True
      if (position.collidelist(pave_num_rects)) == 12 :#clique sur un nombre du pavé numérique : quitter
        remove_current_problem('horloge')
        #return True

###################################################################################fonctions cadenas
def get_code_liste():
  return _liste_code_cadenas

def compare_code():
  if _liste_code_cadenas == _reponse_probleme_cadenas:
    #remove_current_problem('cadenas')
    conditions[4] = True 
    print(conditions)
    give_item("frag_clef_2")
    print("bravo vous avez trouvé le bon code!")
    set_timer_afficher_texte_sans_voix()
    set_texte_sans_voix("bravo vous avez trouvé le bon code!")
  elif _liste_code_cadenas == _fausse_reponse_probleme_cadenas:
    set_timer_afficher_texte_sans_voix()
    set_texte_sans_voix("BRAVO! ah non... CHEH!")
    print("BRAVO! ah non... CHEH!")
    _liste_code_cadenas[0] = "0"
    _liste_code_cadenas[1] = "0"
    _liste_code_cadenas[2] = "0"
  else:
    print("ca n'a pas l'air de fonctionner")
    stop_all_sounds()
    play_sound(nom_voix_inspecteur_pas_fonctionner,1)
    _liste_code_cadenas[0] = "0"
    _liste_code_cadenas[1] = "0"
    _liste_code_cadenas[2] = "0"
def change_code(ligne):
  if _liste_code_cadenas[ligne] == "9":
    _liste_code_cadenas[ligne] = "0"
  else:
    _liste_code_cadenas[ligne] = str(int(_liste_code_cadenas[ligne])+1)
      
def check_pave_cadenas(position):
  for e in get_current_problems():
    if e == "cadenas":
      if position.collidelist(cadenans_button_rects) == 0 :
        change_code(0)
      if position.collidelist(cadenans_button_rects) == 1 :
        change_code(1)
      if position.collidelist(cadenans_button_rects) == 2 :
        change_code(2)
      if position.collidelist(cadenans_button_rects) == 3 :
        compare_code()
      if position.collidelist(quit_button_rects) == 1:
        remove_current_problem("cadenas")
        
###########################################################################fonctions livre
def get_pos_depart():
  global _pos_depart
  return _pos_depart
def set_pos_depart(position):
  global _pos_depart
  _pos_depart = position

def get_texte_se_deplace():
  global _texte_se_deplace
  return _texte_se_deplace

def get_pos_fausse_equation():
  global _pos_fausse_equation
  return _pos_fausse_equation
  
def set_pos_fausse_equation(position):
  global _pos_fausse_equation
  global _rect_fausse_equation
  _pos_fausse_equation = position
  _rect_fausse_equation = pygame.Rect(position[0],position[1],215,142)

def check_pave_livre(position,event):
  global _texte_se_deplace
  for e in get_current_problems():
    if e == "livre":
      if event.type == MOUSEBUTTONUP:
        if position.collidelist(quit_button_rects) == 0:
          remove_current_problem("livre")
        _texte_se_deplace = False
      if event.type == MOUSEBUTTONDOWN:
        
        rect = pygame.Rect(position[0],position[1], 30, 30)
        if rect.colliderect(_rect_fausse_equation):
          set_pos_depart(position)
          _texte_se_deplace = True
   
def get_inventory_se_deplace():
  global _frag_key_1_se_deplace
  global _frag_key_2_se_deplace   
  return [_frag_key_1_se_deplace,_frag_key_2_se_deplace]
  
def get_pos_key_1():
  global _pos_key_1
  return _pos_key_1
  
def set_pos_key_1(position):
  global _pos_key_1
  global _rect_key_1
  _rect_key_1 = pygame.Rect(position[0],position[1],80,79)
  _pos_key_1 = position
  
def get_pos_key_2():
  global _pos_key_2
  return _pos_key_2
  
def set_pos_key_2(position):
  global _pos_key_2
  global _rect_key_2
  _rect_key_2 = pygame.Rect(position[0],position[1],80,79)
  _pos_key_2 = position
      
def check_inventory(position,event):
  global _frag_key_1_se_deplace
  global _frag_key_2_se_deplace
  global _rect_key_1
  global _rect_key_2
  if all(get_conditions()):
    if event.type == MOUSEBUTTONUP:
      _frag_key_1_se_deplace = False
      _frag_key_2_se_deplace = False
      if _rect_key_1.colliderect(_rect_key_2):
        remove_inventory_item("frag_clef_1")
        remove_inventory_item("frag_clef_2")
        _rect_key_1 = pygame.Rect(0,0,0,0)
        _rect_key_2 = pygame.Rect(0,0,0,0)
        give_item("full_key")
    if event.type == MOUSEBUTTONDOWN:
      set_pos_depart(position)
      rect = pygame.Rect(position[0],position[1], 30, 30)
      if rect.colliderect(_rect_key_1): #collide le frag key 1
        _frag_key_1_se_deplace = True 
      elif rect.colliderect(_rect_key_2): #collide le frag key 2
        _frag_key_2_se_deplace = True

if all(conditions):
  print("Vous avez survécu au premier level")



