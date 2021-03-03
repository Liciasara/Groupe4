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
bouton_demarrer = tk.Button(racine, text="Démarrez", font = ("times", "30"), relief="groove")
bouton_arreter = tk.Button(racine, text="Arrêtez", font = ("times", "30"), relief="groove")
bouton_terrain = tk.Button(racine, text="Terrain", font = ("times", "30"), relief="groove")
bouton_etape = tk.Button(racine, text="Étape", font = ("times", "30"), relief="groove")
bouton_sauvegarde = tk.Button(racine, text="Sauvegarde", font = ("times", "30"), relief="groove")
bouton_charge = tk.Button(racine, text="Charge", font = ("times", "30"), relief="groove")

# Placement des widgets

canvas.grid(row=0, column=0, columnspan=3)
bouton_demarrer.grid(row=1, column=0)
bouton_arreter.grid(row=2, column=0)
bouton_terrain.grid(row=1, column=2)
bouton_etape.grid(row=2, column=2)
bouton_sauvegarde.grid(row=1, column=1)
bouton_charge.grid(row=2, column=1)

# Événements

"""Trace le quadrillage"""
quadrillage()

racine.mainloop()