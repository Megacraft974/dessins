from turtle import *
def triangle(taille=200, couleur="red",angle=60):
    "fonction qui dessine un triangle de taille et de couleur determinées,l'angle est 60"
    color(couleur)
    d = 0
    up()
    right(angle)
    while d <3:
        down()
        forward (taille)
        left(120)
        d = d +1
