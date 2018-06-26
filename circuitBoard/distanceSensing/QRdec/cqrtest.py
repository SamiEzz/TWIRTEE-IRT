from numpy import *
from math import pi


def leastSquareQR():
    """
    A=[[12,-5,1],[2,-40,3],[-70,1,1],[89,69,-1],[20,60,-2]]
    B=[2037,5757,1581,-1047,-3510]
    dans ce cas x=[06,06,1995]
    """
    A=[[12,-5,1],[2,-40,3],[-70,1,1],[89,69,-1],[20,60,-2]]
    B=[2037,5757,1581,-1047,-3510]

    x1=[]
    q,r=linalg.qr(A)
    #print(q)
    #print(r)
    
    rinv=linalg.inv(r)
    qtrns=transpose(q)
    x1=matmul(rinv,qtrns)
    print(matmul(x1,B)) #--------------

    """"
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
    """
leastSquareQR()