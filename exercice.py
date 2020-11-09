#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values(start, stop) -> np.ndarray:
    return np.linspace(start, stop, num=64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:
    polar = np.zeros([len(cartesian_coordinates), 2])

    for i in range(len(cartesian_coordinates)):
        rayon = np.sqrt(cartesian_coordinates[i][0] ** 2 + cartesian_coordinates[i][1] ** 2)
        angle = np.arctan2(cartesian_coordinates[i][1], cartesian_coordinates[i][0])
        coordonees = (rayon, angle)
        polar[i] = coordonees

    return polar

def find_closest_index(values: np.ndarray, number: float) -> int:
    return np.abs(values - number).argmin()


#    return 0


if __name__ == '__main__':
    print(linear_values(-1.3, 2.5))
    print(coordinate_conversion([(0, 0), (10, 10), (2, -1)]))
    values_test = np.array([1, 3, 8, 12])
    number_test = 9.5
    print(find_closest_index(values_test, number_test))
    pass




#1. Créer un array présentant 64 valeurs uniformément réparties entre -1.3 et 2.5.

#2. Créer une fonction qui convertit une liste de coordonnées cartésiennes (x, y) 
#en coordonnées polaires (rayon, angle).

#3. Créer un programme qui trouve l’index de la valeur la plus proche d’un nombre 
#fournit dans un array.

#4. Créer un graphe de y=𝑥^2  sin⁡(1∕𝑥^2 )+𝑥 dans l’intervalle [-1, 1] avec 250 points.

#5. Évaluer l’intégrale ∫_(−∞)^∞ 𝑒^(−𝑥^2) 𝑑𝑥. Afficher dans un graphique ∫𝑒^(−𝑥^2) 𝑑𝑥 
#pour x = [-4, 4].