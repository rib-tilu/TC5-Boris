from classes import *
import numpy as np

###############################################################################
#                             CHAMP MAGNÉTIQUE                                #
###############################################################################

def B_uniforme(vB, position, t):
    
    return vB

###############################################################################
#                             CHAMP ÉLECTRIQUE                                #
###############################################################################

def E_uniforme(rE, iE, position, t):
    
    return rE



def E_onde_plane(rE, iE, pulsation, position, t):
    
    return (rE.produit(np.cos(pulsation*t))).plus(iE.produit(np.sin(pulsation*t)))