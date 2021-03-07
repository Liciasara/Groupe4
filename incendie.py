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
import random

#######################################
# Constantes (écrites en majuscule)

LARGEUR = 500
HAUTEUR = 500
COTE = 50
COLONE = 10
LIGNE = 10
COULEUR_QUADR = "grey60"
COLOR_TERRAIN = ["blue", "green", "yellow"]

#######################################
# Variables globales

Tableau = []

#######################################
# Fonctions

def quadrillage(COLONE, LIGNE, COTE):
    """Dessine un quadrillage dans le canevas avec des carrés de côté COTE"""
    global Tableau
    x0 = 0
    y0 = 0
    x1 = COTE
    y1 = COTE
    for i in range(LIGNE) :
        for j in range(COLONE) :
            Tableau[i][j][2] = canvas.create_rectangle((x0, y0), (x1, y1), fill="white", outline="black")
            x0 += COTE
            x1 += COTE
        x0 = 0
        x1 = COTE
        y0 += COTE
        y1 += COTE

def initial_tableau(Tableau, COLONE, LIGNE) :
    """Créé un tableau à double entrée de liste"""
    for i in range (LIGNE) : 
        i = []
        Tableau.append(i)
        for j in range (COLONE) :
            j = ["", 0, 0]
            i.append(j)

def terrain(Tableau) :
    """Remplit le terrain avec une couleur choisie aléatoirement dans COLOR_TERRAIN et l'enregistre dans Tableau """
    for i in range(len(Tableau)) :
        for j in range(len(Tableau[i])) :
            Tableau[i][j][0] = COLOR_TERRAIN[random.randint(0, 2)]
            canvas.itemconfigure(Tableau[i][j][2], fill=Tableau[i][j][0])

def met_le_feu(event) :
    """Remplace la couleur du terrain par du rouge"""
    global Tableau, COTE
    xclic, yclic = event.x, event.y
    col = xclic // COTE
    lig = yclic // COTE 
    if Tableau[lig][col][0] != "blue" :
        Tableau[lig][col][0] = "red"
        canvas.itemconfigure(Tableau[lig][col][2], fill="red")
        print(Tableau)

#######################################
# Programme principale

racine = tk.Tk()
racine.title("Incendie")

# Création des widgets

canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg="white")

bouton_demarrer = tk.Button(racine, text="Démarrez", font = ("times", "30"), relief="groove")
bouton_arreter = tk.Button(racine, text="Arrêtez", font = ("times", "30"), relief="groove")
bouton_terrain = tk.Button(racine, text="Terrain", font = ("times", "30"), relief="groove", command=lambda : terrain(Tableau))
bouton_etape = tk.Button(racine, text="Étape", font = ("times", "30"), relief="groove")
bouton_sauvegarde = tk.Button(racine, text="Sauvegarde", font = ("times", "30"), relief="groove")
bouton_charge = tk.Button(racine, text="Charge", font = ("times", "30"), relief="groove")

initial_tableau(Tableau, COLONE, LIGNE)
quadrillage(COLONE, LIGNE, COTE)

# Placement des widgets

canvas.grid(row=0, column=0, columnspan=3)
bouton_demarrer.grid(row=1, column=0)
bouton_arreter.grid(row=2, column=0)
bouton_terrain.grid(row=1, column=2)
bouton_etape.grid(row=2, column=2)
bouton_sauvegarde.grid(row=1, column=1)
bouton_charge.grid(row=2, column=1)

# Événements

canvas.bind("<Button-1>", met_le_feu)

racine.mainloop()