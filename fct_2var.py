#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:25:10 2021

@author: Saadia Bayou
"""


# Imports 
import numpy as np
import matplotlib.pyplot as plt

# Fonction à 2 variables
def fxy (x,y):
    #cercle
    return x**2+y**2



# Dimensions repère
x=np.arange(-10,10)
y=np.arange(-10,10)

# Maillage
X,Y=np.meshgrid(x,y)

# Équation du cercle - fonction à deux variables
z=fxy(X,Y)

# Tracé cercles
plt.contourf(X,Y,z)
# Titres et légendes
plt.title("Graphe fxy")

plt.xlabel("Axe des absicces")
plt.ylabel("Axe des ordonnées")
# Sauvegarde
plt.savefig("Fig1-Graphe.png")
# Visualisation
plt.colorbar()
plt.show()


# Tracé contours cercles
plt.contour(X,Y,z)
# Titre et légendes
plt.title("Contours fxy")
plt.xlabel("Axe des abscisses")
plt.ylabel("Axe des ordonnées")
# Sauvegarde
plt.savefig("Fig2-Contours.png")
# Visualisation
plt.show()
