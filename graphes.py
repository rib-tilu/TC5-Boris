import numpy as np
import matplotlib.pyplot as plt



def plot_1d_graphs(listeX, listeY, titre, titreX, titreY):
    
    plt.plot(np.array(listeX), np.array(listeY), color='green', label=titre)
    
    plt.xlabel(titreX)
    plt.ylabel(titreY)
    
    plt.legend()
    
    plt.show()
    
    return None



def plot_1d_trajs(listeX, listeY, titre, titreX, titreY):
    
    plt.plot(np.array(listeX), np.array(listeY), color='red', label=titre)
    
    plt.xlabel(titreX)
    plt.ylabel(titreY)
    
    plt.title(titre)
    
    plt.show()
    
    return None



def plot_3d(listeX, listeY, listeZ, titre, titreX, titreY, titreZ):
    
    ax = plt.axes(projection='3d')
    
    ax.plot3D(np.array(listeX), np.array(listeY), np.array(listeZ), 'gray')
    
    plt.title(titre)
    
    ax.set_xlabel(titreX, fontsize=13)
    ax.set_ylabel(titreY, fontsize=13)
    ax.set_zlabel(titreZ, fontsize=13)
    
    plt.show()
    
    return None
