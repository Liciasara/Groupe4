#######################################
# groupe Bi TD-04
# BENKHEROUF Licia
# DERIAN Filina
# STAELENS Pauline
# GUERFA Sarah
# https://github.com/Liciasara/Groupe4
#######################################

#######################################
# Import des librairies

import tkinter as tk

#######################################
# Constantes (écrites en majuscule)

LARGEUR = 500
HAUTEUR = 500
COTE = 10
COULEUR_QUADR = "grey60"

#######################################
# Variables globales

#######################################
# Fonctions

def quadrillage():
    """Dessine un quadrillage dans le canevas avec des carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    x = 0
    while x <= LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        x += COTE

#######################################
# Programme principale

racine = tk.Tk()
racine.title("Incendie")

# Création des widgets

canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="white")

# Placement des widgets

canvas.grid()

# Événements

"""Trace le quadrillage"""
quadrillage()

racine.mainloop()