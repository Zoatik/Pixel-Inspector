import pygame
from fonctions.loading import* #pour le debugger

class Animation:

    def __init__(self, fenetre, image_filenames, interval, cycle=True):
        self.images = []
        for image_filename in image_filenames:
            self.images.append(pygame.image.load(image_filename).convert_alpha())
        self.fenetre = fenetre
        self.interval = interval
        self.init_interval = interval
        self.index = 0
        self.cycle = cycle
        self.last_blit = 0

    def get_current_surface(self):
        return self.images[self.index]

    def blit_one_frame(self, frame, area):
      if frame < len(self.images) : 
        self.fenetre.blit(self.images[frame],area)
      else:
        debug_message("classe_animation", "21", "index out of range")
    def blit(self, area, interval):
      t = pygame.time.get_ticks()
      if interval == 0:
        self.interval = self.init_interval #si interval == 0 on veut blit à la fréquence de l'initialisation

      if t - self.last_blit > self.interval:
        if self.index < (len(self.images) - 1):
          self.index += 1
        else:
          self.index = 0
        self.last_blit = t
      self.fenetre.blit(self.get_current_surface(), area)
        

