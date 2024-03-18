import pygame
from pygame.locals import *

_inventory = {}

def reset_inventory():
  global _inventory
  _inventory = {}

def give_item(item):
  _inventory[item] = True
  print("vous avez obtenu un nouvel objet:", item)
  
def get_inventory():
  return _inventory
  
def is_in_inventory(item):
  check = False
  for e in _inventory:
    if item == e:
      check = True
  return check


def remove_inventory_item(nom_item):
  if nom_item in _inventory:#contrôle que l'objet à supprimer est bien dans l'inventaire
    del _inventory[nom_item]  
    print("cet objet n'est plus dans votre inventaire:" , nom_item)
  else:
    print(f"ERREUR {nom_item} n'est pas dans l'inventaire")
  