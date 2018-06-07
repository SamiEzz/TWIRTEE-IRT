"""
__________________________________________________________________________________________________________
|#########################################################################################################|
|##																										##|
|##																										##|
|##																										##|
|##			Simulation du calcul de la position par Trilateration										##|
|##																										##|
|##																										##|
|##			Tuteur	: JENN Eric																			##|
|##			Auteur	: EZZEROUALI Sami																	##|
|##																										##|
|#########################################################################################################|

"""


import matplotlib.pyplot as plt
from numpy import *
from math import *




def anchorsPosition(delta):
	"""
	Cette fonction defini la position de l'emeteur i en _Xa[i],_Ya[i]
	_Xa,_Ya deux lists de coordonnees vides (a definir avant l'appel de la fonction)

	++TODO:	Rendre la fonction adaptable en nombre d'emetteurs, en suivant les methodes
			de placement evoque dans "Roa et al. - 2007 - Optimal placement of sensors for trilateration Re"
	"""
	_Xaux=[0,0,delta,delta]
	_Yaux=[0,delta,delta,0]
	_position=[_Xaux,_Yaux]
	return _position;



vector=anchorsPosition(1000)
"""
print vector
plt.plot(vector[0],vector[1],"d",markersize=30)
plt.show()
"""









































