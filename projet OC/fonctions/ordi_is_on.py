from constantes import *

_ordi_is_on = False

#######################################
### LAG QUAND SPAM ALLUMER/ETEINDRE ###
#######################################

def get_ordi_is_on():
  global _ordi_is_on
  return _ordi_is_on

def set_ordi_is_on(on_off):
  global _ordi_is_on
  _ordi_is_on = on_off