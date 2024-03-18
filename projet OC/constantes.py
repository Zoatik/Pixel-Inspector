import pygame
from pygame.locals import *
pygame.font.init()


titre_fenetre = "Pixel Inspector"
fenetre = pygame.display.set_mode((1000,933))

#rectangles colisions lvl1
collisions = [
  pygame.Rect(160,360,226,120),
  pygame.Rect(391,303,205,105),
  pygame.Rect(566,411,203,67),
  pygame.Rect(716,479,60,162),
  pygame.Rect(646,579,68,90),
  pygame.Rect(558,623,85,60),
  pygame.Rect(467,675,88,92),
  pygame.Rect(391,734,76,73),
  pygame.Rect(319,768,69,71),
  pygame.Rect(194,728,126,108),
  pygame.Rect(152,628,85,98),
  pygame.Rect(124,477,73,150)]
#tableau qui cree le mur lvl1
#collisions = [const_rect_1,const_rect_2,const_rect_3,const_rect_4,const_rect_5,const_rect_6,const_rect_7,const_rect_8,const_rect_9,const_rect_10,const_rect_11,const_rect_12]

#####################################################
### stockage des noms/chemins d'acces aux images  ###
#####################################################
####################################personnage
nom_tete = "images/personnage/tete.png"
nom_personnage_idles = [
  "images/personnage/idle_1.png",
  "images/personnage/idle_2.png",
  "images/personnage/idle_3.png",
  "images/personnage/idle_4.png"] 
####################################decor accueil
nom_bord_loupe = "images/decor_accueil/bord_loupe.png"
nom_fond_accueil = "images/decor_accueil/accueil.png"


####################################decor lvl_1
nom_etagere = "images/decor_lvl_1/etagere.png"
nom_fond_lvl_1 = "images/decor_lvl_1/fond.png"
nom_fond_lvl_1_censored = "images/decor_lvl_1/fond_censored.jpg"
nom_pilier = "images/decor_lvl_1/pilier.png"
nom_lit = "images/decor_lvl_1/lit.png"
nom_icone = "images/PI.png"
nom_horloge = "images/decor_lvl_1/horloge.png"
nom_lampe_on = "images/decor_lvl_1/lampe_on.png"
#####################################objets inventaire
nom_frag_key_1_lvl_1 = "images/keys/frag_key_1_lvl_1.png"
nom_frag_key_2_lvl_1 = "images/keys/frag_key_2_lvl_1.png"
nom_full_key_lvl_1 = "images/keys/full_key_lvl_1.png"
nom_outil_horloge = "images/decor_lvl_1/outil_horloge.png"
rects_inventory = [
  pygame.Rect(10,10,78,79),
  pygame.Rect(100,10,78,79)]
#####################################interface 
nom_quit_button = "images/interface/quit_button.png"
quit_button_rects = [
  pygame.Rect(758,244,20,20),#livre
  pygame.Rect(494,517,20,20)]#cadenas
nom_livre = "images/interface/livre.png"
livre_rect = pygame.Rect(595,379,70,35)
nom_vraie_equation = "images/interface/vraie_equation.png"
nom_fausse_equation = "images/interface/fausse_equation.png"
nom_texte_ennui= "images/interface/texte_ennui.png"
nom_pave_numerique = "images/interface/pave_numerique.png"
pave_num_rects = [
  pygame.Rect(477,545,50,50), #0
  pygame.Rect(384,352,50,50), #1
  pygame.Rect(477,352,50,50), #2
  pygame.Rect(570,352,50,50), #3
  pygame.Rect(384,417,50,50), #4
  pygame.Rect(477,417,50,50), #5
  pygame.Rect(570,417,50,50), #6
  pygame.Rect(384,480,50,50), #7
  pygame.Rect(477,480,50,50), #8
  pygame.Rect(570,480,50,50), #9
  pygame.Rect(384,568,30,25), #supprimer
  pygame.Rect(578,557,70,30), #enter
  pygame.Rect(660,230,30,20)] #quitter
cadenans_button_rects = [
  pygame.Rect(579,400,20,20),
  pygame.Rect(579,433,20,20),
  pygame.Rect(579,467,20,20),
  pygame.Rect(461,336,90,40)]
nom_chronometre = "images/interface/chronometre.png"
nom_box_text = "images/interface/box_text.png"
pos_box = (270,70)
pos_texte = (280,80) 
nom_press_e = "images/interface/press_e.png"
nom_cadenas_closed = "images/interface/cadenas_closed.png"
nom_cadenas_open = "images/interface/cadenas_open.png"
nom_cadenas_button = "images/interface/next_button.png"
#####################################curseur animé
nom_cursors = [
  "images/cursors/cursor_1.png",
  "images/cursors/cursor_2.png",
  "images/cursors/cursor_3.png"]
#####################################décors animés
nom_ordis_on = [
  "images/decor_lvl_1/ordi_1.png",
  "images/decor_lvl_1/ordi_2.png"]
nom_ordis_off = [
  "images/decor_lvl_1/ordi_1_pause.png",
  "images/decor_lvl_1/ordi_2_pause.png"]
nom_tete_robot = "images/decor_lvl_1/tete_robot.png"
#####################################bords surbrillance
nom_bord_ordi = "images/decor_lvl_1/bord_ordi.png"
nom_bord_tirelire = "images/decor_lvl_1/bord_tirelire.png"
nom_bord_pilier = "images/decor_lvl_1/bord_pilier.png"
nom_bord_horloge = "images/decor_lvl_1/bord_horloge.png"

#####################################polices de texte
loading_font = pygame.font.SysFont('Comic Sans MS',30)
texte_font = pygame.font.SysFont("Comic Sans MS", 15)
timer_font = pygame.font.Font("fonts/brightly_crush_shine.otf", 40)
code_font  = pygame.font.SysFont('franklingothicheavyitalique', 22)
enter_font = pygame.font.Font("fonts/brightly_crush_shine.otf", 25)
nombres_pave_surfaces = {
  (497,545):timer_font.render("0",False,(165,42,42)),
  (404,352):timer_font.render("1",False,(165,42,42)),
  (497,352):timer_font.render("2",False,(165,42,42)),
  (590,352):timer_font.render("3",False,(165,42,42)),
  (404,417):timer_font.render("4",False,(165,42,42)),
  (497,417):timer_font.render('5',False,(165,42,42)),
  (590,417):timer_font.render("6",False,(165,42,42)),
  (404,480):timer_font.render("7",False,(165,42,42)),
  (497,480):timer_font.render("8",False,(165,42,42)),
  (590,480):timer_font.render("9",False,(165,42,42)),
  (577,557):enter_font.render("ENTRER",False,(165,42,42))}

fin_temps_font = pygame.font.Font("fonts/brightly_crush_shine.otf", 100)
#####################################event rects 
event_rect_action_tirelire = pygame.Rect(520, 615, 52, 57)
event_rect_action_horloge = pygame.Rect(562,256,50,60)
event_rect_action_variable = pygame.Rect(317,419,50,20)
event_rect_action_ordi = pygame.Rect(694,358,40,60)
event_rect_action_pilier = pygame.Rect(134,448,80,250)
event_rect_action_lampe = pygame.Rect(855,451,40,60)
event_rect_action_tete_robot = pygame.Rect(260,352,100,50)
event_rect_action_loupe = pygame.Rect(321, 598, 185, 176)
event_rect_action_dict = {"tirelire":event_rect_action_tirelire, "horloge":event_rect_action_horloge, "variable":event_rect_action_variable, 
"ordi":event_rect_action_ordi, "pilier":event_rect_action_pilier, "lampe": event_rect_action_lampe,"tete_robot": event_rect_action_tete_robot,"loupe": event_rect_action_loupe}
event_rect_action_press_e_dict = {"tirelire":event_rect_action_tirelire,"pilier":event_rect_action_pilier}
#####################################event rects interfaces clics
event_rect_interface_horloge = pygame.Rect(324,232,359,386)

######################################musiques
nom_musique_accueil = "musiques/accueil/accueil.mp3"
musiques_lvl_1 = ["musiques/lvl_1/ambiance_1.mp3"]
######################################voix
nom_voix_pix_fascine_horloge = "voix/pix/fascine.wav"                                               #########################################
nom_voix_pix_aide = "voix/pix/aide.wav"                                                             ### ATTENTION: les .wav ne peuvent    ###
nom_voix_pix_remercier = "voix/pix/tirelire_remercier.wav"                                          ### pas être top complexes. Solution: ###
nom_voix_pix_tirelire_dire = "voix/pix/dire.wav"                                                    ### convertir en .mp3 puis de nouveau ###
nom_voix_inspecteur_pas_fonctionner = "voix/personnage/pas_fonctionner.wav"   
nom_voix_tirelire_enfin_qqun = "voix/cochon/enfin_qqun.wav"  
nom_voix_tirelire_pas_le_time = "voix/cochon/pas_le_time.wav"
nom_voix_tirelire_si_tu_te_poses_la_question = "voix/cochon/si_tu_te_poses_la_question.wav"
nom_voix_tirelire_remercier = "voix/cochon/tiens_pour_te_remercier.wav"                             ### en .wav                           ###
                                                                                                    #########################################

#####################################################################sons
nom_sound_ordi = "musiques/lvl_1/ennui_ordi.wav"  
#####################################################################bruitages
nom_bruitage_orage_pluie = "sons/lvl_1/orage_pluie.wav"     
liste_bruitages_lvl_1 = {"pluie_tonnerre": nom_bruitage_orage_pluie}                                                 
nom_bruitage_porte_closed = "sons/lvl_1/porte_bloque.wav"
nom_bruitage_porte_open = "sons/lvl_1/porte_ouvre.wav"
nom_bruitage_pas_marche = "sons/lvl_1/pas_marche.wav"
nom_bruitage_pas_course = "sons/lvl_1/pas_course.wav"
######################################textes pix lvl 1
texte_1 = "cette tirelire semble vouloir dire quelque chose..."
texte_2 = "Il faut qu'on l'aide!"
texte_3 = "La tirelire semble vouloir te remercier"
texte_4 = "cette tirelire a l'air d'etre fascinée par les aiguilles de la montre!"
texte_5 = "ça n'a pas l'air de fonctionner..."
texte_cochon_1 = "Enfin quelqu'un... vite dépêche-toi de réparer l'horloge!"
texte_cochon_2 = "Ne reste pas planté là, je n'ai pas ton temps, moi!"
texte_cochon_3 = "si tu te poses la question, NON! "
texte_cochon_4 = "Ah! Enfin! J'attendais ça depuis longtemps. Tiens."
texte_lecture_en_cours= "Lecture en cours..."
 
######################################dict voix-texte
voix_texte = {nom_voix_pix_tirelire_dire: texte_1, nom_voix_pix_aide: texte_2, nom_voix_pix_remercier: texte_3, nom_voix_pix_fascine_horloge: texte_4, nom_voix_inspecteur_pas_fonctionner : texte_5,
               nom_voix_tirelire_enfin_qqun: texte_cochon_1, nom_voix_tirelire_pas_le_time: texte_cochon_2, nom_voix_tirelire_si_tu_te_poses_la_question: texte_cochon_3, nom_voix_tirelire_remercier: texte_cochon_4}
#voix_texte = {nom_voix_pix_aide: texte_2}
#voix_texte = {nom_voix_pix_remercier: texte_3}
#voix_texte = {nom_voix_pix_fascine_horloge: texte_4}





















































