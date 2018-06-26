
class Position(object):
    def __init__(self,rate=0.05):
        self.plotNum = 4           #
        self.anchors = []          # [_Xaux,_Yaux]                                       / anchorsPosition() //
        self.ray=[]                # [[R11,,,R1n],...,[Rm1,...,Rmn]]                     / rightPosition()
        self.mray=[]               # [[R11,,,R1n],...,[Rm1,...,Rmn]]                     / distanceSensors()
        self.rate = rate           # 0 < rate < 1                                        / input
        self.mode = 1              # 1,2,3 ?                                             / input
        self.cercles=[]            # [[Cx1,..,Cxn],[Cy1,...,Cyn]] n=720*len(ray[0])      / drawCercles()
        self.robotXY = []          # [[x1,..,xn],[y1,..,yn]]                             / robotMove()
        self.A=[]                  # [[A11,A12],...,[An1,An2]]                           / computeAB() \\ A est unique pour chaque shèma de balises
        self.b=[]                  # [[b11,...,b1n],...,[bm1,...,bmn]] m100,n4           / computeAB()  \\ b est unique pour chaque point du robot
        self.approXY = []          # [[x0,..,xn],[y0,..,yn]]                             / computeAB() -> leastSuareQR() /
        self.error=[[],[],[],[],[],[]]

def serialConnect(){
    
}