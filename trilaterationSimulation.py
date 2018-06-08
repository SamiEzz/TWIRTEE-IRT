"""
_______________________________________________________________________________
|##																			##|
|##																			##|
|##																			##|
|##			Simulation du calcul de la position par Trilateration			##|
|##																			##|
|##																			##|
|##			Tuteur	: JENN Eric												##|
|##			Auteur	: EZZEROUALI Sami										##|
|##																			##|
|#############################################################################|
"""


import matplotlib.pyplot as plt
from numpy import *
from random import * # randint(0,10) return a random value 0<X<10
#from math import *

#----- System constant --------------
delta=1000
Ray=[1700,1150,300,1300]
noise=0.1

#------------------------------------

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
vector=anchorsPosition(delta)

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
	plt.plot(cx,cy,"--",color="skyBlue")
	plt.show()


def robotMove():
	t=linspace(0,10,5)
	x=100*(t)+200
	y=(t)**3+200
	plt.plot(x,y,"D",markersize=10,color="green")
	print "Last robot cordinates :"
	print [x[4],y[4]]

def distanceSensors(rate,ray):
	dvector=[]
	for i in range(len(ray)):
		dvector.append(ray[i]+randint(-rate*ray[i],rate*ray[i]))
	return dvector;

#print distanceSensors(0.1,[1000,1000,1000,1000])

def makeA(anchorsVector):
	"""

	"""
	_x=anchorsVector[0]
	_y=anchorsVector[1]

	A=[]
	for i in range(1,len(_x)):
		A.append([_x[i]-_x[0],_y[i]-_y[0]])
	return A

#print makeA(vector)


def makeB(ray,anchorsVector):
	b=[]
	_x=anchorsVector[0]
	_y=anchorsVector[1]


	for i in range(1,len(ray)):
		b.append(0.5*(ray[0]**2-ray[i]**2+(_x[i]-_x[0])**2+(_y[i]-_y[0])**2))
	return b

print makeA(vector)

def matMult(A,B):
	"""
	"""

def computeXY(sensRay,vector,noiseRate):
	"""
	"""
	x=[]
	xminusx0=[]
	A=makeA(vector)
	B=makeB(sensRay,vector)



# -------- Functions call
robotMove()
xAnchors=vector[0]
yAnchors=vector[1]


plt.plot(xAnchors,yAnchors,"o",markersize=15,color="red")

sensRay=distanceSensors(noise,Ray)
print Ray
print sensRay

drawCercles(xAnchors,yAnchors,sensRay)
#computeXY(sensRay,vector,noise)
robotMove()
plt.plot(xAnchors,yAnchors,"o",markersize=15,color="red")
drawCercles(xAnchors,yAnchors,Ray)


















