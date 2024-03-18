import pygame
import time
from pygame.locals import *
from pygame import mixer

#from constantes import *
from fonctions.afficher_level import*
from fonctions.movement import*
from fonctions.timer_projet import*
#from fonctions.check_activity import*
#from fonctions.loading import*
#from fonctions.cooldown_event import *
from fonctions.clic_souris import*
#from fonctions.gestionnaire_musique import*
from classes.classe_animation import*

pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
def reset_lvl_1():
  reset_enigme_lvl_1()
  reset_inventory()

# with open("sauvegarde.txt","r") as fichier_sauvegarde:
  # contenu = fichier_sauvegarde.read()
  # print (contenu)
  # contenu = contenu.split(", \'.\'")
  # contenu_conditions = contenu[0]
  # print (contenu_conditions)
  # print (contenu_conditions.find("False"))
  # fichier_sauvegarde.close()


PIXEL_INSPECTOR = True
while PIXEL_INSPECTOR:
  MOVE_SPEED_X = 5
  MOVE_SPEED_Y = 5
  LOOK = 0  # direction du personnage entre 1 et 4 : 1:s/ 2:d/ 3:w/ 4:a
  LVL = 0
  PERSO_RECT = pygame.Rect(345, 515, 67, 129) #rectangle de collision de notre personnage
  PERSO_RECT_ACCUEIL = pygame.Rect(300, 515, 67, 129)
  PIX_RECT_ACCUEIL = pygame.Rect(400,515,30,30)
  ARRET_ACCUEIL= False
  ARRET_JEU = False
  
  personnage_accueil_anim = Animation(fenetre, nom_personnage_idles,200)
  pix_accueil_anim = Animation(fenetre,nom_cursors,210)
########################################################################################### ACCUEIL
  play_music(nom_musique_accueil,0.5)
  
  while not ARRET_ACCUEIL:#boucle accueil
    creation_level(LVL)
    personnage_accueil_anim.blit(PERSO_RECT_ACCUEIL, 0)
    pix_accueil_anim.blit(PIX_RECT_ACCUEIL, 0)
    for event in pygame.event.get():
      if event.type == QUIT:
       ARRET_ACCUEIL = True
       ARRET_JEU = True
       PIXEL_INSPECTOR = False
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          ARRET_ACCUEIL = True
      if event.type == MOUSEBUTTONUP:
        if (get_mouse_rect().collidedict(event_rect_action_dict,1)) == ("loupe", event_rect_action_loupe):
          ARRET_ACCUEIL = True
    display.flip()
  fadeout_music()
  #time.sleep(2)#pour l'instant évite que la musique de l'accueil se superpose avec la musique du jeu

########################################################################################### TRANSITION ACCUEIL/LEVEL
  if not ARRET_JEU:#controle si le joueur a quitte avant le lancement du level
    LVL = 1
    INTERVAL = pygame.time.get_ticks()
    #ARRET_JEU = loading(LVL)
    creation_level(LVL)
    start_timer = get_timer()#retourne le temps actuel pour le timer
    TIMER = (start_timer,pygame.time.get_ticks())
    TIME_COOLDOWN = pygame.time.get_ticks()#pour le cooldown des events
    pygame.key.set_repeat(10, 30)

    play_a_random_song(musiques_lvl_1)
    
    

########################################################################################### BOUCLE DE JEU
  while not ARRET_JEU:#boucle de jeu
    #pygame.time.Clock().tick(45)  #limite les tours de boucle par sec et evite des problemes de lag

    ## EVENEMENTS
    for event in pygame.event.get():
      if event.type == QUIT:
       ARRET_JEU = True
       PIXEL_INSPECTOR = False
      if event.type == SONG_END:
        play_a_random_song(musiques_lvl_1)
      if event.type == KEYDOWN:
        if event.key == K_w or event.key == K_s or event.key == K_a or event.key == K_d:
          
          mouvement = movement(event,PERSO_RECT,LOOK,MOVE_SPEED_X,MOVE_SPEED_Y)
          PERSO_RECT = mouvement[0] #PERSO_RECT recoit la position
          LOOK = mouvement [1] #LOOK recoit la direction
        if event.key == K_e:
          if cooldown_event(TIME_COOLDOWN,1000):#cooldown entre deux interractions : retourne True si l'interval est suffisant
            check_activity_key(PERSO_RECT,event)#controle si le joueur interragit avec le décor en appuyant sur "e"
            TIME_COOLDOWN = set_cooldown_event()
        if event.key == K_i:
          if cooldown_event(TIME_COOLDOWN,100):
            TIME_COOLDOWN = set_cooldown_event()
      if event.type == KEYUP:
        if event.key == K_w or event.key == K_a or event.key == K_d or event.key == K_s:
          stop_bruitage(nom_bruitage_pas_marche,2)
      if event.type == MOUSEBUTTONUP:
        clic_souris(event)
      if event.type == MOUSEBUTTONDOWN:
        clic_souris(event)
        
    ##ACTIONS 
    set_currently_playing_bruitage(1)
    play_random_bruitage(liste_bruitages_lvl_1,1)    #on utilise le cannal 1 pour les bruitages en back ground
    move_object()
    refresh_level(LVL,PERSO_RECT)
    TIMER = timer(300 ,start_timer,TIMER[1])
    if not TIMER[0]:#contrôle si le temps est écoulé
      ARRET_JEU = True
      reset_lvl_1()
      
      
    ##AFFICHAGE
    pygame.display.flip() #on met à jour l'affichage

with open("sauvegarde.txt","w") as fichier_sauvegarde:
  contenu = fichier_sauvegarde.write(str(get_current_enigme_lvl_1()))

  fichier_sauvegarde.close()
    #direction(LOOK)
    
    

         
