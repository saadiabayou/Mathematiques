#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:25:10 2021

@author: Saadia Bayou
"""

# Imports 
import numpy as np
import matplotlib.pyplot as plt

# Fonction de 2 variables
def cercle (x,y):
    """ Calcul le rayon d'un cercle de centre O(0,0)"""
    r=x**2+y**2
    return r

# Dimensions repère
x=np.arange(-10,11)
y=np.arange(-10,11)

# Maillage
X,Y=np.meshgrid(x,y)

# Équation du cercle - fonction à deux variables
z=cercle(X,Y)

# Tracé cercles
plt.figure(1)
fig1=plt.contourf(X,Y,z)
# Titres et légendes
plt.title("Rayon du cercle - 2D")
plt.xlabel("x")
plt.ylabel("y")
# Sauvegarde
plt.savefig("Fig1-distribution rayon.png")
# Visualisation
plt.colorbar(fig1)
plt.show()


## Tracé contours cercles
plt.figure(2)
fig2=plt.contour(X,Y,z)
# Titre et légendes
plt.title("Cercles")
plt.xlabel("x")
plt.ylabel("y")
# Sauvegarde
plt.savefig("Fig2-Contours-cercle.png")
# Visualisation
plt.show()
