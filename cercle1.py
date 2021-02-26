#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:25:10 2021

@author: Saadia Bayou
"""


# Imports 
import numpy as np
import matplotlib.pyplot as plt

# Fonction cercle
def cercle(x,y):
    r=x**2+y**2
    return r


# Dimensions repère
x=np.arange(-10,10)
y=np.arange(-10,10)

# Maillage
X,Y=np.meshgrid(x,y)

# Équation du cercle - fonction à deux variables
R=cercle(X,Y)

# Tracé cercles
plt.contourf(x,y,R)
# Titres et légendes
plt.title("Rayons-cercles")

plt.xlabel("Axe des absicces , x")
plt.ylabel("Axe des ordonnées, y ")
# Sauvegarde
plt.savefig("Rayons.png")
# Visualisation
plt.colorbar()
plt.show()


# Tracé contours cercles
plt.contour(X,Y,R)

# Titre et légendes
plt.title("Contours rayons - cercles")
plt.xlabel("Axe des abscisses ")
plt.ylabel("Axe des ordonnées ")
# Sauvegarde
plt.savefig("Contours-rayons.png")
# Visualisation
plt.show()
