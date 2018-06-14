import matplotlib.pyplot as plt
from numpy import *
from math import pi
from random import *

class test(object):
    def __init__(self,rate=0.05):
        self.plotNum = 4           #
        self.anchors = anchors     # [_Xaux,_Yaux]               / anchorsPosition() //
        self.robotXY = robotXY     # [[x0,..,xn],[y0,..,yn]]     / robotMove()
        self.approXY = [[],[]]     # [[x0,..,xn],[y0,..,yn]]     / computeAB() -> leastSuareQR() /
        self.rate = rate           # 0 < rate < 1                / input
        self.mode = mode           # 1,2,3 ?                     / input
        self.A=[]                  # [[A00,A01],...,[An0,An1]]   / computeAB()
        self.b=[]                  # [b1,...,bn]                 / computeAB()
        self.ray=[]                #                             / rightPosition()
        self.mray=[]               # []                            /

    def anchorsPosition(self,delta):
        _Xaux=[0,0,delta,delta]
        _Yaux=[0,delta,delta,0]
        self.anchors=[_Xaux,_Yaux]

    def rightRayons(self):
        for i in range(len(self.anchors[1])):
            xyanchor=array((0,0))
            xyanchor[0]=self.anchors[0][i]
            xyanchor[1]=self.anchors[1][i]
            self.ray.append(linalg.norm(xyanchor-position))

    def distanceSensors(self):
        for i in range(len(self.ray)):
            self.mray.append(self.ray[i]+randint(-int(self.ray[i]*self.rate)-1,int(self.ray[i]*self.rate+1)))

    def computeAB(self,anchors):
        position=[0,0]
        _x=self.anchors[0]
        _y=self.anchors[1]
        A=[]
        for i in range(1,len(_x)):
            A.append([_x[i]-_x[0],_y[i]-_y[0]])
        b=[]
        for i in range(1,len(self.ray)):
            b.append(0.5*(self.ray[0]**2-self.ray[i]**2+(_x[i]-_x[0])**2+(_y[i]-_y[0])**2))
        self.A=A
        self.b=b

    def leastSquareQR(self):
        q,r=linalg.qr(self.A)
        rinv=linalg.inv(r)
        qtrns=transpose(q)
        x1=matmul(rinv,qtrns)
        self.approXY=matmul(x1,self.b)

    def robotMove(self):
        t=linspace(0,10,100)
        x=(-500+250*t)*0.8
        y=0.8*(500+800*sin(t))
        self.robotXY.append(x)
        self.robotXY.append(y)
