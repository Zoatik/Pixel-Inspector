import time
from constantes import *
from fonctions.loading import *



def timer(length,start,prev_time):
  running = True
  countdown = int(length - (time.time() - start))
  if countdown > 0:
    timer_surface = timer_font.render (str(countdown),False,(0,250,0))
    fenetre.blit(timer_surface,(880,10))
  else:
    timer_surface = fin_temps_font.render ("FIN DU TEMPS",False,(250,0,0))
    fenetre.blit(timer_surface,(200,400))
  if time.time() - prev_time > 1:
    prev_time = time.time()
    if countdown <= 0:
      running = False
       
 
  return (running,prev_time)

if __name__ == '__main__':
    timer(300)


def get_timer():
  return time.time()






























































