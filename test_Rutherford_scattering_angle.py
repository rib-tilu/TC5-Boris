# This script compares the analytical Coulomb scattering angle with the numerical
# one calculated with the Boris algorithm with more and more points to demonstrate
# the convergence of our scheme towards the correct solution
#
# BE CAREFUL RUNNING THIS SCRIPT TOOK MY COMPUTER 1H14 !!

from classes import *
import numpy as np
from graphesN import *
from champs import E_noyau as f_E



### Numerical constants ###


Nt = [] ## number of time steps list

dt = 1e-17 ## time step (s)

DT = dt/2


### Physical constants ###


q = 2*(1.602*10**(-19)) ## particle charge (C)

m = 6.644657e-27 ## particle mass (kg)

Z = +79 ## heavy nucleus atomic number Z

r = 135e-12 ## heavy nucleus atomic radius (cm)



def propage1(position_init, vitesse_init, N_step): ## single particle full propagation on N_step time steps


    traj_x, traj_y, traj_z = [], [], []
    
    V_x, V_y, V_z = [], [], []
    
    X = position_init
    
    V = vitesse_init
    
    Ec, temps = [], []
    
    
    for k in range(N_step):
        
        Xinter = X.plus(V.produit(DT))
        
        B = Vector(0, 0, 0)
        
        E = f_E(Z, Xinter)
        
        
        phase = step(Xinter, V, B, E, q, m, dt) # storing array for [X,V] vectors
        
        
        X = phase[0]
        
        V = phase[1]
        
        
        traj_x.append(X.x*100)
        traj_y.append(X.y*100)
        
    if traj_x[-1] < 0 and traj_y[-1] == 0:
    
        return 180
    
    else:
        
        return 2*180*np.arctan(traj_y[-1]/(traj_x[-1] + (traj_x[-1]**2 + traj_y[-1]**2)**0.5))/np.pi



def propage_N(N, bmax, N_step): ## N particles propagation with a variation of impact parameter

    
    # liste_b = np.linspace(bmax/N, bmax, N)
    
    liste_b = np.linspace(0, bmax, N)
    
    liste_phi = []
    
    for i in range(N):
        
        bi = liste_b[i]
        
        ### INITIALISATION ### 
        
        # vecteur position initiale (m)

        X0 = Vector(-5e-8, bi, 0)


        # vecteur vitesse initiale (m/s)

        V0 = Vector(1000000, 0, 0)

        # stockage de l'angle de diffusion (deg)

        liste_phi.append(propage1(X0, V0, N_step))
        
    
    
    mu = 3.27e-25*m/(3.27e-25+m)

    K = q*Z*1.602e-19/(4*np.pi*8.85e-12*(1000000**2)*mu)
    
    # calcul de l'angle de diffusion par la formule de Rutherford (deg)
    
    listeY = 2*180*np.arctan(K/liste_b)/np.pi
    
    
    return abs(np.array(liste_phi[-1]) - listeY[-1])/min(listeY[-1], liste_phi[-1])


Nt = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 4800, 4900, 4910, 4920, 4930, 4940, 4950, 4960, 4970, 4980, 4990, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]



E = []

for e in Nt:
    
    E.append(propage_N(500, 500e-12, e))
    
plt.plot(np.array(Nt), np.array(E))

plt.xlabel(r'Number of time steps')
plt.xscale('log')

plt.ylabel('Relative error')
plt.yscale('log')

plt.grid(True, which="both")

plt.show()