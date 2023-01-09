# Ces fonctions sont les mêmes que celles de graphes, mais sans les plt.show(), afin de construire les titres
# échelles et légendes indépendemment dans le main

import numpy as np
import matplotlib.pyplot as plt



def plot_2d_graphs(listeX, listeY):
    
    plt.plot(np.array(listeX), np.array(listeY), color='green')
    
    return None



def plot_2d_trajs(listeX, listeY):
    
    plt.plot(np.array(listeX), np.array(listeY), color='red')
    
    return None



def plot_3d(listeX, listeY, listeZ):
    
    ax = plt.axes(projection='3d')
    
    ax.plot3D(np.array(listeX), np.array(listeY), np.array(listeZ), 'gray')
    
    return None



def plot_2D(listeX, listeY):
    
    plt.plot(np.array(listeX), np.array(listeY))
    
    return None
