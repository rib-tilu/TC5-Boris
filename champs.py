# Fonctions donnant les expressions des champs E ou B utilisés

from classes import *
import numpy as np

###############################################################################
#                             CHAMP ÉLECTRIQUE                                #
###############################################################################

def E_noyau(Znoy, pos): # singe nucleus located at the origin
    
    return pos.produit((Znoy*1.602e-19)/(4*np.pi*8.85e-12*(pos.norm()**3)))



###############################################################################
#                             CHAMP MAGNÉTIQUE                                #
###############################################################################

