from turtle import *
def etoile():
      chiffre = 0
      while chiffre <12:
            down()
            forward(100)
            left(150)
            chiffre = chiffre +1
b = 0
while b <10:
      etoile()
      up()
      left(60)
      forward(150)
      b = b +1
 
    
