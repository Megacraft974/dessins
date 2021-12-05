# -*- coding: utf-8 -*-
from dessins_tortue import *
up() # relever le crayon
goto(-150, 50) # reculer en haut à gauche
# dessiner dix carrés rouges, alignés :
i= 0
while i < 10:
    down()
    carre(25, 'red')
    up()
    forward(30)
    i = i +1
a = input()
# abaisser le crayon
    # tracer un carré
    # relever le crayon
    # avancer + loin
    # attendre
