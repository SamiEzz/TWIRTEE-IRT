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
	++TODO:	Rendre la fonction adaptable en nombre d'emetteurs, en suivant les methodes
			de placement evoque dans "Roa et al. - 2007 - Optimal placement of sensors for trilateration Re"
	"""
	_Xaux=[0,0,delta,delta]
	_Yaux=[0,delta,delta,0]
	_position=[_Xaux,_Yaux]
	return _position;



vector=anchorsPosition(1000)

xAnchors=vector[0]
yAnchors=vector[1]

plt.plot(xAnchors,yAnchors,"o",markersize=15)
#plt.show()

def drawCercles(_X,_Y,_R):
	"""

	"""
	ome=linspace(0,2*pi,720);
	i=0
	cx=[]
	cy=[]
	for k in range(4):
		for i in range(720):
			cx.append(_X[k]+_R[k]*sin(ome[i]))
			cy.append(_Y[k]+_R[k]*cos(ome[i]))
	plt.plot(cx,cy,"--")
	# plt.show()

Ray=[1000*sqrt(2),1000,0,1000]
drawCercles(xAnchors,yAnchors,Ray)

def robotMove():
	t=linspace(0,10,100)
	x=100*t
	y=t**3
	plt.plot(x,y)
	plt.show()
robotMove()

def computeXY():
	"""
		-- bruit rand pour simuler les capteurs de distance
	"""
def distanceSensors():
	dvector=[]






















