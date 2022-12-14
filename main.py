from classes import *
import numpy as np
from graphes import *
from champs import B_uniforme as f_B
from champs import E_uniforme as f_E


### Constantes numériques ###


Nt = 100 ## nombre de pas temporels

Nc = 20 ## nombre de pas par orbite


### Constantes physiques ###


q = 1*(-1.602*10**(-19)) ## charge de la particule (C)

m = 9.1095*10**(-31) ## masse de la particule (kg)

omega = 2*np.pi*10**10 ## pulsation de l'onde plane (rad/s)


###############################################################################
#                           INITIALISATION                                    #
###############################################################################

# vecteur position (m)

X = Vector(0,0,0)


# vecteur vitesse (m/s)

V = Vector(1000000, 1000000, 1000000)


# tableaux pour stocker les paramètres de la trajectoire

traj_x, traj_y, traj_z = [], [], []

V_x, V_y, V_z = [], [], []

Ec, Mu, Rlarmor, temps = [], [], [], []


# versions stationnaires des champs magnétique et électrique (parties réelle et imaginaire)

B = Vector(0, 0, m*omega/abs(q))

RE = Vector(100000, 0, 100000)

IE = Vector(0,0,0)



dt = 2*np.pi*m/(abs(q)*B.norm()*Nc) ## pas temporel (s) verifiant dt < 2/omega_c

DT = dt/2


###############################################################################
#                      PROPAGATION DE LA PARTICULE                            #
###############################################################################



for k in range(Nt):
    
    Xinter = X.plus(V.produit(DT))
    
    B = f_B(B, Xinter, k*dt)
    
    E = f_E(RE, IE, Xinter, k*dt)
    
    
    phase = step(Xinter, V, B, E, q, m, dt) # tableau pour stocker [X,V]
    
    
    X = phase[0]
    
    V = phase[1]
    
    
    traj_x.append(X.x*100)
    traj_y.append(X.y*100)
    traj_z.append(X.z*100)
    
    V_x.append(V.x)
    V_y.append(V.y)
    V_z.append(V.z)
    
    
    Ec.append( m*produit_scalaire(V, V)/(2*abs(q)) )
    
    Rlarmor.append( 100*m*( (produit_scalaire( produit_vectoriel( produit_vectoriel(V,B) , B ) , produit_vectoriel( produit_vectoriel(V,B) , B ) ))**0.5 )/(abs(q)*(B.norm()**3)) )

    Mu.append( m*produit_scalaire( produit_vectoriel( produit_vectoriel(V,B) , B ) , produit_vectoriel( produit_vectoriel(V,B) , B ) )/(2*(B.norm()**5)) )
    
    temps.append(dt*k*10**12)



###############################################################################
#                            TRACÉS DE GRANDEURS                              #
###############################################################################

plot_1d_trajs(traj_x, traj_y, "Trajectoire dans le plan (x,y)", "x [cm]", "y [cm]")

plot_1d_trajs(traj_z, traj_y, "Trajectoire dans le plan (y,z)", "z [cm]", "y [cm]")

plot_3d(traj_x, traj_y, traj_z, "Trajectoire 3D", "X (cm)", "Y (cm)", "Z (cm)")


# plot_1d_trajs(temps, V_x, "Vx", "t [ps]", r"Vx [m.s$^{-1}$]")

# plot_1d_trajs(temps, V_y, "Vy", "t [ps]", r"Vy [m.s$^{-1}$]")

# plot_1d_trajs(temps, V_z, "Vz", "t [ps]", r"Vz [m.s$^{-1}$]")


plot_1d_graphs(temps, Ec, "Energie cinétique", "t [ps]", "Ec [eV]")

plot_1d_graphs(temps, Rlarmor, "Rayon de Larmor", "t [ps]", "Rl [cm]")

plot_1d_graphs(temps, Mu, "Moment magnetique", "t [ps]", r"$\mu$ [A.m$^{2}$]")