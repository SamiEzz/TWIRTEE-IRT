import matplotlib.pyplot as plt
from numpy import *
from math import *
from time import sleep

"""
-----
	Tuteur	: JENN Eric
	Auteur	: EZZEROUALI Sami
"""


# Variables du systeme et de la simulation


dt=0.01;
iterations=600;
k=0;

h=100;
L=2;
x0=0
y0=0
teta0=0
Vl=[]
Vr= []

#	Construction des vecteurs de commande Vr,Vl
for k in range(0,50):
	Vl.append(k/50)
	Vr.append(k/25)
for k in range(0,50):
	Vl.append(0.5)
	Vr.append(0)
for k in range(0,200):
	Vl.append(1)
	Vr.append(1)
for k in range(0,50):
	Vl.append(0.5)
	Vr.append(1)
for k in range(0,250):
	Vl.append(1)
	Vr.append(1)

plt.plot(linspace(0,10,600),Vl)
plt.plot(linspace(0,10,600),Vr)
plt.show()
"""
plt.plot(linspace(0,10,60),Vr)
plt.show()
"""

#Vecteurs d etat X=(x,y,teta)

x=[];
y=[];
z=[];
teta=[]

x.append(0)
y.append(0)
teta.append(0)

for k in range(1,iterations):
	x.append(x[k-1]+h/2*(Vr[k-1]+Vl[k-1])*cos(teta[k-1]))
	y.append(y[k-1]+h/2*(Vr[k-1]+Vl[k-1])*sin(teta[k-1]))
	teta.append(teta[k-1]+h/L*(Vr[k-1]-Vl[k-1]))
plt.plot()
i=0;
while 1==1:
    if i == 0:
        line, = plt.plot(x, y,teta)
    else:
        line.set_ydata(y)
    plt.pause(0.01) # pause avec duree en secondes
    i=1

plt.show()
