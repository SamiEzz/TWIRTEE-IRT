# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:22:03 2018

@author: Sami
"""

import matplotlib.pyplot as plt
from numpy import *
from math import pi
from random import *

class test(object):
    def __init__(self,rate=0.05):
        self.plotNum = 4           #
        self.anchors = []          # [_Xaux,_Yaux]                                       / anchorsPosition() //
        self.ray=[]                # [[R11,,,R1n],...,[Rm1,...,Rmn]]                     / rightPosition()
        self.mray=[]               # [[R11,,,R1n],...,[Rm1,...,Rmn]]                     / distanceSensors()
        self.rate = rate           # 0 < rate < 1                                        / input
        self.mode = 0              # 1,2,3 ?                                             / input
        self.cercles=[]            # [[Cx1,..,Cxn],[Cy1,...,Cyn]] n=720*len(ray[0])      / drawCercles()
        self.robotXY = []          # [[x1,..,xn],[y1,..,yn]]                             / robotMove()
        self.A=[]                  # [[A11,A12],...,[An1,An2]]                           / computeAB() \\ A est unique pour chaque shèma de balises
        self.b=[]                  # [[b11,...,b1n],...,[bm1,...,bmn]] m100,n4           / computeAB()  \\ b est unique pour chaque point du robot
        self.approXY = []          # [[x0,..,xn],[y0,..,yn]]                             / computeAB() -> leastSuareQR() /
    
    
    def anchorsPosition(self,delta):
        _Xaux=[0,0,delta,delta]
        _Yaux=[0,delta,delta,0]
        self.anchors=[_Xaux,_Yaux]

    def rightRayons(self):
        self.ray=[]
        for k in range(len(self.robotXY[0])):
            auxray=[]
            position=[]
            for i in range(len(self.anchors[1])):
                xyanchor=array((0,0))
                xyanchor[0]=self.anchors[0][i]
                xyanchor[1]=self.anchors[1][i]
                position.append([self.robotXY[0][k],self.robotXY[1][k]])
                auxray.append(linalg.norm(xyanchor-position[i]))
            self.ray.append(auxray)

    def distanceSensors(self):
        self.mray=[]
        for k in range(len(self.robotXY[0])):
            auxmray=[]
            for i in range(len(self.anchors[1])):
                auxmray.append(self.ray[k][i]+randint(-int(self.ray[k][i]*self.rate)-1,int(self.ray[k][i]*self.rate+1)))
            self.mray.append(auxmray)
    def computeA(self):
        self.A=[]
        _x=self.anchors[0]
        _y=self.anchors[1]
        A=[]
        for i in range(1,len(_x)):
            A.append([_x[i]-_x[0],_y[i]-_y[0]])
        self.A=A
    def computeAB(self):
        _x=self.anchors[0]
        _y=self.anchors[1]
        self.computeA()
        self.b=[]
        for k in range(len(self.robotXY[0])):
            auxb=[]
            for i in range(1,len(self.mray[0])):
                auxb.append(0.5*(self.mray[k][0]**2-self.mray[k][i]**2+(_x[i]-_x[0])**2+(_y[i]-_y[0])**2))
            
            self.b.append(auxb)
    def leastSquareQR(self):
        x1=[]
        q,r=linalg.qr(self.A)
        rinv=linalg.inv(r)
        qtrns=transpose(q)
        x1=matmul(rinv,qtrns)
        #print(x1) #--------------
        position=[]
        newx=[]
        newy=[]
        self.approXY=[]
        for k in range(len(self.robotXY[0])):
            position.append(matmul(x1,self.b[k]))
            newx.append(position[0][0])
            newy.append(position[0][1])
            position=[]
        self.approXY.append(newx)
        self.approXY.append(newy)
        
        

    def robotMove(self):
        t=linspace(0,10,100)
        x=(-500+250*t)*0.8
        y=0.8*(500+800*sin(t))
        self.robotXY.append(x)
        self.robotXY.append(y)

    def drawCercles(self,_R): # _R = mray or ray \\ "test.drawCercles(test.mray)"
        teta=linspace(0,2*pi,720);
        cx=[]
        cy=[]
        for k in range(len(self.anchors[0])):
            for i in range(len(teta)):
                cx.append(self.anchors[0][k]+_R[k]*sin(teta[i]))
                cy.append(self.anchors[1][k]+_R[k]*cos(teta[i]))
        self.cercles=[cx,cy]

test1=test(0.01)
test1.anchorsPosition(1000)
test1.robotMove()
test1.rightRayons()
test1.distanceSensors()
test1.computeAB()

test1.leastSquareQR()
test1.drawCercles(test1.mray[50])

plt.grid(True)
plt.plot(test1.robotXY[0],test1.robotXY[1])
plt.plot(test1.approXY[0],test1.approXY[1],"+")

plt.plot(test1.cercles[0],test1.cercles[1])

plt.plot(test1.anchors[0],test1.anchors[1],"P",markersize=15)
#print(test1.approXY[0][0])
