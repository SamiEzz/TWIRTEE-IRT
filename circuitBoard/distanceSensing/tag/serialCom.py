import serial
<<<<<<< HEAD
import os
clear = lambda: os.system('cls')

distances = open("distances.txt","w")
distances.write("id , distance\n")
anchors=[]
distances=[]
=======


>>>>>>> 5c8bedd5322ebf97608e11a56510e674f08c58cc

#=======================Class def======================================
class TAG(object):
    def __init__(self):
        self.sline=-1
        #self.lastState=-1
        self.devices=[]
        self.theBigMatrix=[]
<<<<<<< HEAD
        self.anchorsNumber=0
        self.anchorsid=[]   #
        self.rangeVal=[]    #
=======

        self.anchorsNumber=0
>>>>>>> 5c8bedd5322ebf97608e11a56510e674f08c58cc
        self.tagPort='/dev/ttyUSB0'
        self.tagBaud=19200
    def loop(self):
        while True:
<<<<<<< HEAD
            id=-1
            range=-1
            if (ser.inWaiting()>0):
                
                var=ser.readline()
                self.sline = var.decode("utf-8")
                ordre=self.sline[0]

                #print("Frame : "+ self.sline[:len(self.sline)-1])
                #print("Ordre : "+ ordre)
                
                if(ordre=="0"):
                    id=self.sline[2:len(self.sline)-1]
                    self.lostDevice(id)
                elif(ordre=="1"):
                    id=self.sline[2:]
                    self.newDevice(id)
                elif(ordre=="2"):
                    idrange=self.sline[2:]
                    id=idrange[:idrange.find(",")]
                    range=idrange[idrange.find(",")+1:len(idrange)-1]
                    self.newRange(id,range)
                #else:
                    #print("useless ordre")
    #def idToNum(self):
    def isKnownId(self):
        while(i<=len(self.anchorsid)):
            if(self.anchorsid[i]==id):
                return True
            i+=1
        
    def newDevice(self,id):
        self.anchorsNumber+=1
        
        i=0
        


        print("new device : "+id)
    def lostDevice(self,id):
        self.anchorsNumber-=1
        while(i<=len(self.anchorsid)):
            if(self.anchorsid[i]==id):
                self.anchorsNumber+=1
            i+=1
        print("Lost device : "+id)
    def newRange(self,id,range):
        while(i<=len(self.anchorsid)):
            if(self.anchorsid[i]==id):
                self.anchorsNumber-=1
            i+=1
        print(id + " : " + range + " [m]")
        distances.write(id + " , " + range +"\n")
=======
            if (ser.inWaiting()>0):
                self.sline = ser.readline()
                print(self.sline)
            

    def newDevice(self,id):
        print("new device : "+id)
    def lostDevice(self):
        print("l")
    def newRange(self):
        print("d")
>>>>>>> 5c8bedd5322ebf97608e11a56510e674f08c58cc
    #-------------------Setters------------------------

    

#=====================================================================
ser = serial.Serial(port="/dev/ttyUSB0", baudrate=19200, timeout=1,writeTimeout=1)
tag = TAG()
tag.loop()
<<<<<<< HEAD
distances.close()
=======


"""
options = { 0:tag.lostDevice,
            1:tag.newDevice,
            2:tag.newRange,
}

with Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=1,writeTimeout=1) as serialTag:
    serialTag.open()
    if serialTag.isOpen():
        while true:
            ligne=serialTag.readline()
            options[ligne[0]]()
            """
#=====================================================================





>>>>>>> 5c8bedd5322ebf97608e11a56510e674f08c58cc



