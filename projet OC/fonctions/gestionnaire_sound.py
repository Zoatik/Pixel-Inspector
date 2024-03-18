import pygame

from constantes import *

_currently_playing_sound = {}#uniquement pour les voix reliées à un texte!!!!
_volume_sound = 0.5
#_currently_playing_bruitages_channel_1 = {}#pour tous les sons d'ambiance
#_currently_playing_bruitages_channel_2 = {}
#_currently_playing_bruitages_channel_3 = {}
_currently_playing_bruitages_all_channels = [{},{},{},{},{}]
_volume_bruitage = 0.1

################canal 0 = voix
################canaux 1 à 3 = bruitages d'ambiance
################canal 4 à 5 = buitages d'interraction



def play_sound(sound_key,volume):
  pygame.mixer.Channel(0).stop()
  play_sound = pygame.mixer.Sound(sound_key)
  play_sound.set_volume(volume)
  _currently_playing_sound[sound_key] = play_sound
  pygame.mixer.Channel(0).play(play_sound)
def fadeout_sound(sound_key,length):#fait un fadeout sur le son donné pour une durée donnée
  pygame.mixer.Channel(0).fadeout(length)
  #_currently_playing_sound[sound_key].fadeout(length)
  del _currently_playing_sound[sound_key]

def stop_sound(sound_key):#stop le son donné en argument s'il est bien en cours d'exécution
  if len(_currently_playing_sound) != 0:
    pygame.mixer.Channel(0).stop()
    del _currently_playing_sound[sound_key]

def stop_all_sounds():#stop tous les sons en cours d'exécution
  global _currently_playing_sound
  sounds_to_remove = []
  while True:#la boucle évite que le dictionnaire change pendant l'itération
    for sound in _currently_playing_sound:  
      _currently_playing_sound[sound].stop()
      sounds_to_remove.append(sound)
    for remove in sounds_to_remove: 
      del _currently_playing_sound[remove]
    break

def set_currently_playing_sound(): #vide la liste des sons si aucun son n'est en cours
  #print(pygame.mixer.Channel(0).get_sound())
  if pygame.mixer.Channel(0).get_sound() == None:
    #print("elle n'est pas busy")
    _currently_playing_sound.clear()

def get_currently_playing_sound():#retourne le dictionnaire de son
  #print (_currently_playing_sound)
  return _currently_playing_sound
  
def get_volume_sound():
  global _volume_sound
  return _volume_sound
  
def set_volume_sound(volume):
  global _volume_sound
  _volume_sound = volume
 
#######################################################################################

def play_bruitage(bruitage_key,volume,canal):
  
  pygame.mixer.Channel(canal).stop()
  play_bruitage = pygame.mixer.Sound(bruitage_key)
  play_bruitage.set_volume(volume)
  if canal == 1: 
    _currently_playing_bruitages_all_channels[0][bruitage_key] = play_bruitage
    pygame.mixer.Channel(canal).play(play_bruitage)
  elif canal == 2:
    _currently_playing_bruitages_all_channels[1][bruitage_key] = play_bruitage
    pygame.mixer.Channel(canal).play(play_bruitage)
  elif canal == 3:
    _currently_playing_bruitages_all_channels[2][bruitage_key] = play_bruitage
    pygame.mixer.Channel(canal).play(play_bruitage)
  elif canal == 4:
    _currently_playing_bruitages_all_channels[3][bruitage_key] = play_bruitage
    pygame.mixer.Channel(canal).play(play_bruitage)
  elif canal == 5:
    _currently_playing_bruitages_all_channels[4][bruitage_key] = play_bruitage
    pygame.mixer.Channel(canal).play(play_bruitage)
  else : 
    print("le canal pour les bruitages ne peut être qu'entre 1 et 5")
    
def fadeout_bruitage(bruitage_key,length, canal):#fait un fadeout sur le son donné pour une durée donnée
  if canal == 1 and len(_currently_playing_bruitages_all_channels[0]) >0:
    _currently_playing_bruitages_all_channels[0][bruitage_key].fadeout(length)
    del _currently_playing_bruitages_all_channels[0][bruitage_key]
  elif canal == 2 and len(_currently_playing_bruitages_all_channels[1]) >0:
    _currently_playing_bruitages_all_channels[1][bruitage_key].fadeout(length)
    del _currently_playing_bruitages_all_channels[1][bruitage_key]
  elif canal == 3 and len(_currently_playing_bruitages_all_channels[2]) >0:
    _currently_playing_bruitages_all_channels[2][bruitage_key].fadeout(length)
    del _currently_playing_bruitages_all_channels[2][bruitage_key]
  else : 
    print("le canal pour les bruitages ne peut être qu'entre 1 et 3")
    
def stop_bruitage(bruitage_key,canal):#stop le son donné en argument s'il est bien en cours d'exécution
  if canal == 1 and len(_currently_playing_bruitages_all_channels[0]) >0:
    _currently_playing_bruitages_all_channels[0][bruitage_key].stop()
    del _currently_playing_bruitages_all_channels[0][bruitage_key]
  elif canal == 2 and len(_currently_playing_bruitages_all_channels[1]) >0:
    _currently_playing_bruitages_all_channels[1][bruitage_key].stop()
    del _currently_playing_bruitages_all_channels[1][bruitage_key]
  elif canal == 3 and len(_currently_playing_bruitages_all_channels[2]) >0:
    _currently_playing_bruitages_all_channels[2][bruitage_key].stop()
    del _currently_playing_bruitages_all_channels[2][bruitage_key]
  elif canal == 4 and len(_currently_playing_bruitages_all_channels[3]) >0:
    _currently_playing_bruitages_all_channels[3][bruitage_key].stop()
    del _currently_playing_bruitages_all_channels[3][bruitage_key]
  elif canal == 5 and len(_currently_playing_bruitages_all_channels[4]) >0:
    _currently_playing_bruitages_all_channels[4][bruitage_key].stop()
    del _currently_playing_bruitages_all_channels[4][bruitage_key]
  else : 
    print("le canal pour les bruitages ne peut être qu'entre 1 et 5")

def stop_all_bruitages_in_channel(canal):#stop tous les sons en cours d'exécution dans un canal (1 à 5)
  global _currently_playing_bruitages
  bruitages_to_remove = []
  while True:#la boucle évite que le dictionnaire change pendant l'itération
    for bruitage in _currently_playing_bruitages_all_channels[canal]:  
      _currently_playing_bruitages_all_channels[canal-1][bruitage].stop()
      bruitages_to_remove.append(bruitage)
    for remove in bruitages_to_remove: 
      del _currently_playing_bruitages_all_channels[canal-1][remove]
    break
 
def play_random_bruitage(liste_bruitages,canal):# pour les bruitages d'ambiance
  lancer_bruitage = True
  for e in get_currently_playing_bruitage(canal):
    for i in liste_bruitages:              # si aucun bruitage contenu dans "liste_bruitages" n'est joué, alors on lance un nouveau bruitage de cette liste
      if e == i : 
        lancer_bruitage = False
     
  if lancer_bruitage == True:    
    if len(liste_bruitages) > 1:
      next_bruitage = random.choice(liste_bruitages)
      new_bruitage = pygame.mixer.Sound(liste_bruitages[next_bruitage])
      new_bruitage.set_volume(get_volume_bruitage())
      _currently_playing_bruitages_all_channels[canal-1][next_bruitage] = new_bruitage
      pygame.mixer.Channel(canal).play(new_bruitage) ######################utilise le canal 1  à 3 pour les bruitages d'ambiance
    elif len(liste_bruitages) == 1: 
      new_bruitage = pygame.mixer.Sound(liste_bruitages["pluie_tonnerre"])
      new_bruitage.set_volume(get_volume_bruitage())
      pygame.mixer.Channel(canal).play(new_bruitage)
      _currently_playing_bruitages_all_channels[canal-1][list(liste_bruitages.keys())[0]] = new_bruitage
    else:
      print("erreur: aucun bruitage dans la liste")

def set_currently_playing_bruitage(canal): #vide la liste des sons si aucun son n'est en cours
  if pygame.mixer.Channel(canal).get_sound() == None:
    #print("elle n'est pas busy")
    _currently_playing_bruitages_all_channels[canal-1].clear()


def get_currently_playing_bruitage(canal):#retourne le dictionnaire de son
  #print (_currently_playing_bruitages_all_channels)
  return _currently_playing_bruitages_all_channels[canal-1]
  
def get_volume_bruitage():
  global _volume_bruitage
  return _volume_bruitage
  
def set_volume_bruitage(volume):
  global _volume_bruitage
  _volume_bruitage = volume
  


  




  
