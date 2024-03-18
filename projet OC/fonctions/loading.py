import pygame
from pygame.locals import *
from constantes import *
from classes.classe_animation import*
###################################################
###### loading.py ne charge pas vraiment les ######
######   éléments. Il faudra le modifier :)  ######
###################################################
pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.key.set_repeat()#accepte de rester appuyer sur une touche du clavier

personnage_idle_anim = Animation(fenetre, nom_personnage_idles,200)
cursor_anim = Animation(fenetre, nom_cursors, 200)
ordi_on_anim = Animation(fenetre, nom_ordis_on, 200)
ordi_off_anim = Animation(fenetre, nom_ordis_off, 200)




tete = pygame.image.load(nom_tete).convert_alpha()
icone = pygame.image.load(nom_icone).convert_alpha()
etagere = pygame.image.load(nom_etagere).convert_alpha()
pilier = pygame.image.load(nom_pilier).convert_alpha()
lit = pygame.image.load(nom_lit).convert_alpha()
lampe_on = pygame.image.load(nom_lampe_on ).convert_alpha()
bord_ordi = pygame.image.load(nom_bord_ordi).convert_alpha()
bord_tirelire = pygame.image.load(nom_bord_tirelire).convert_alpha()
bord_pilier = pygame.image.load(nom_bord_pilier).convert_alpha()
bord_horloge = pygame.image.load(nom_bord_horloge).convert_alpha()
fond = pygame.image.load(nom_fond_lvl_1).convert()
fond_censored = pygame.image.load(nom_fond_lvl_1_censored).convert()
horloge = pygame.image.load(nom_horloge).convert_alpha()
frag_key_1_lvl_1 = pygame.image.load(nom_frag_key_1_lvl_1).convert_alpha()
frag_key_2_lvl_1 = pygame.image.load(nom_frag_key_2_lvl_1).convert_alpha()
full_key_lvl_1 = pygame.image.load(nom_full_key_lvl_1).convert_alpha()
outil_horloge = pygame.image.load(nom_outil_horloge).convert_alpha()
box_text = pygame.image.load(nom_box_text).convert_alpha()
chronometre = pygame.image.load(nom_chronometre).convert_alpha()
pave_numerique = pygame.image.load(nom_pave_numerique).convert()
cadenas_closed = pygame.image.load(nom_cadenas_closed).convert_alpha()
cadenas_open = pygame.image.load(nom_cadenas_open).convert_alpha()
cadenas_button = pygame.image.load(nom_cadenas_button).convert_alpha()
livre = pygame.image.load(nom_livre).convert_alpha()
quit_button = pygame.image.load(nom_quit_button).convert_alpha()
vraie_equation = pygame.image.load(nom_vraie_equation).convert_alpha()
fausse_equation = pygame.image.load(nom_fausse_equation).convert_alpha()
texte_ennui = pygame.image.load(nom_texte_ennui).convert_alpha()
press_e = pygame.image.load(nom_press_e)
press_e.fill((255, 255, 255, 180), special_flags=BLEND_RGBA_MULT)#met en transparence l'image
tete_robot = pygame.image.load(nom_tete_robot).convert_alpha()
bord_loupe = pygame.image.load(nom_bord_loupe).convert_alpha()
fond_accueil = pygame.image.load(nom_fond_accueil)

def debug_message(fichier, ligne, type_erreur):

  print(f"ERREUR : dans le fichier \"{fichier}\" à la ligne {ligne}. Problème avec : {type_erreur}")
  

# def loading(lvl):
  # loading_surface = loading_font.render ('Loading',False,(250,250,250))
  # fenetre.blit(loading_surface,(400,400))
  # pygame.display.flip()
  # print(pygame.font.get_fonts())

    
  # chargement = True
  # while chargement:
    # for event in pygame.event.get(): 
      # if event.type == QUIT:
        # arret = True
        # chargement = False
      # if event.type == KEYDOWN:
        # if event.key == K_RETURN:
          # arret = False
          # chargement = False
          
     
  # pygame.key.set_repeat(10, 30)
  # return arret


