import pygame
import random

from constantes import *

_currently_playing_song = None
_last_music = None
_music_volume = 0.3

def set_music_volume(intensity):
  global _music_volume
  _music_volume = intensity
  
def get_music_volume():
  global _music_volume
  return _music_volume

def play_music(music_key,volume):
  global _currently_playing_song
  pygame.mixer.music.load(music_key)
  pygame.mixer.music.set_volume(get_music_volume())
  pygame.mixer.music.play()
  _currently_playing_song = music_key
  
def fadeout_music():
  global _currently_playing_song
  pygame.mixer.music.fadeout(1000)
  _currently_playing_song = None

def stop_music():
  global _currently_playing_song
  pygame.mixer.music.stop()
  _currently_playing_song = None

def get_currently_playing_song():
  global _currently_playing_song
  return _currently_playing_song
  
def play_a_random_song(music_list):
  global _currently_playing_song
  next_song = _currently_playing_song
  if len(music_list) > 1:
    while next_song == _currently_playing_song:
        next_song = random.choice(music_list)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.set_volume(get_music_volume())
    pygame.mixer.music.play()
  elif len(music_list) == 1:
    pygame.mixer.music.load(music_list[0])
    pygame.mixer.music.set_volume(get_music_volume())
    pygame.mixer.music.play()
  else:
    print("erreur: pas de musique dans la liste")
      
    
