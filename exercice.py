#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as mp
from scipy.integrate import quad 


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



#moi
def graphique():
    x = np.linspace(-1, 1,  num = 250)
    y = x**2 * np.sin(1/x**2) + x
    mp.plot(x, y, ".", markersize = 2.5)
    mp.show()
#--------------------------------------------------------
#prof
def exercise_sin() -> None:
    graph_sinusoid_sample(*samples_from_function(sinusoid, -1, 1, 250))

def graph_sinusoid_sample(x: np.ndarray, y: np.ndarray):
    mp.plot(x, y, ".", markersize = 2.5)
    mp.legend(["data"], loc= "best")
    mp.show()

def samples_from_function(func: callable, start: float, end: float, nb_samples: int) -> tuple:
    x = np.linspace(start, end, num=nb_samples, endpoint=True)
    y = np.array([func(x_i) for x_i in x])

    return x, y

def sinusoid(x: float) -> float:
    return x**2 * np.sin(1/x**2) + x
#---------------------------------------------------------
#5. Évaluer l’intégrale ∫_(−∞)^∞ 𝑒^(−𝑥^2) 𝑑𝑥. Afficher dans un graphique 
# ∫𝑒^(−𝑥^2) 𝑑𝑥 pour x = [-4, 4].
def integration(a, b):
    return quad(integrand, a, b)

def integrand(x: np.ndarray) -> np.ndarray:
    return np.exp(-x**2)



if __name__ == '__main__':
    #print(linear_values(-1.3, 2.5))
    #print(coordinate_conversion([(0, 0), (10, 10), (2, -1)]))
    #values_test = np.array([1, 3, 8, 12])
    #number_test = 9.5
    #print(find_closest_index(values_test, number_test))
    #graphique()
    #exercise_sin()
    #print(integration(-np.inf, np.inf))
    pass




